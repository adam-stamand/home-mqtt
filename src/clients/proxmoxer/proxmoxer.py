import sys
from proxmoxer import ProxmoxAPI
import time
from src.clients.common.MQTTClient import MQQTClient as MC
import util.credentialCrypt as CC
import yaml
from pathlib import Path

def connect_cb(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("Sys/proxmox/request")

def message_cb(client, userdata, message):
    print("Message received: {}".format(message.payload))
    msgList = message.payload.decode("utf-8").split(":")
    if len(msgList) != 2:
        print("Unable to parse proxmox message")
        return 
    vmid = msgList[0]
    action = msgList[1]

    rv = proxmox.nodes('prox').qemu(vmid).status.post(action)



def ConnectProxmox():
    cwd = Path(__file__).resolve().parents[3]
    conf = yaml.load(open(str(cwd / "conf/credentials.yml")))
    
    addr = conf['proxmox-server']['address'].encode('utf-8')
    pwd = conf['proxmox-server']['password'].encode('utf-8')
    
    key = CC.load_key(str(cwd / "conf/key.key"))
    addr = CC.decrypt(addr, key).decode('utf-8')
    pwd = CC.decrypt(pwd, key).decode('utf-8')
    
    return ProxmoxAPI(addr, user='root@pam',
                        password=pwd, verify_ssl=False)


def ConnectMQTT():
    client = MC("proxmoxer", clean_session=False)
    client.on_connect = connect_cb
    client.on_message = message_cb
    client.connect("192.168.1.114", port=1883, keepalive=60)
    client.loop_start()
    return client

def Loop(proxmox, client):
    while True:
        time.sleep(5)
        buffer = ""

        for vm in proxmox.cluster.resources.get(type='vm'):
            buffer += ("{0}. {1} => {2}\n" .format(vm['vmid'], vm['name'], vm['status']))

        msgInfo = client.publish("Sys/proxmox/status", buffer, qos=0)

        try:
            msgInfo.wait_for_publish()
        except Exception as e:
            print(e)

def main():
    proxmox = ConnectProxmox()
    mqttClient = ConnectMQTT()
    Loop(proxmox, mqttClient)
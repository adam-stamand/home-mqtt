import paho.mqtt.client as mqtt
import logging


class MQQTClient(mqtt.Client):
        
    def __init__(self, client_id="", clean_session=None, userdata=None,
                 protocol=mqtt.MQTTv311, transport="tcp", logginglevel=logging.INFO):
        
        logging.basicConfig(level=logginglevel)
        self.logger = logging.getLogger("{}-logger".format(client_id))
        self.logger.setLevel(logginglevel)



        super().__init__(
            client_id=client_id, 
            clean_session=clean_session, 
            userdata=userdata,
            protocol=protocol, 
            transport=transport)
        
        self.on_connect = self.default_connect_cb
        self.on_publish = self.default_publish_cb
        self.on_subscribe = self.default_subscribe_cb
        self.on_unsubscribe = self.default_unsubscribe_cb
        self.on_disconnect = self.default_disconnect_cb
        self.on_message = self.default_message_cb
    
    def default_connect_cb(self, client, userdata, rc):
        self.logger.info("Connected with result code {}".format(rc))
    
    def default_disconnect_cb(self, client, userdata, rc):
        self.logger.info("Disconnected with result code {}".format(rc))

    def default_publish_cb(self, client, userdata, mid):
        self.logger.info("Published with message id {}".format(mid))

    def default_subscribe_cb(self, client, userdata, mid, granted_qos):
        self.logger.info("Subscribed with qos {} with result code {}".format(qos, mid))

    def default_unsubscribe_cb(self, client, userdata, mid):
        self.logger.info("Unsubcribed with message id {}".format(mid))

    def default_message_cb(self, client, userdata, message):
        self.logger.info("Message received: {}".format(message))






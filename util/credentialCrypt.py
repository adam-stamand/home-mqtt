from cryptography.fernet import Fernet
from pathlib import Path


def write_key(fileName):
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open(fileName, "wb") as key_file:
        key_file.write(key)

def load_key(fileName):
    """
    Loads the key from the current directory named `key.key`
    """
    return open(fileName, "rb").read()

def encrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    # encrypt data
    return Fernet(key).encrypt(file_data)
    
def decrypt(data, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    # decrypt data
    return Fernet(key).decrypt(data)



from os.path import exists
from cryptography.fernet import Fernet


def readFile(fileName):
    if not exists(fileName):
        return ''
    with open(fileName, 'rb') as f:
        return encryptionKey().decrypt(f.read()).decode()


def saveToFile(content, fileName):
    encrypted = encryptionKey().encrypt(str.encode(content))
    with open(fileName, 'wb') as f:
        f.write(encrypted)


def encryptionKey():
    KEY_FILE = 'local-data/filekey.key'

    if exists(KEY_FILE):
        with open(KEY_FILE, 'rb') as filekey:
            return Fernet(filekey.read())

    key = Fernet.generate_key()

    # string the key in a file
    with open(KEY_FILE, 'wb') as filekey:
        filekey.write(key)

    return Fernet(key)

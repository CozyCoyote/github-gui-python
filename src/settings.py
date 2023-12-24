from os.path import exists
import encrypt_utils

TOKEN_FILE = "local-data/.token"


def token():
    if not exists(TOKEN_FILE):
        return ""
    return encrypt_utils.readFile(TOKEN_FILE)


def saveToken(token):
    return encrypt_utils.saveToFile(token, TOKEN_FILE)


def hostname():
    return "github.com"


def savedProjects():
    return ["Apples", "Oranges"]

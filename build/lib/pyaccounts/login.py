import time
import json
import hashlib
import os

"""Login to an account with user defined details:"""
def loginui():
    if os.path.exists("Data") == False:
        os.mkdir("Data")
    user = input("What's your username?\n")
    password = input("What's your password?\n")
    f = open("Data/{}.json".format(user), "r")
    content = f.read()
    content = json.loads(content)
    m = hashlib.md5()
    encoded = password.encode('utf-8')
    m.update(encoded)
    if str(m.digest()) == content["password"]:
        print("Successfully logged in")
        return

    else:
        print("Incorrect username or password")
        raise ValueError('Incorrect username or password')
        return

"""Login to an account with software defined details"""
def login(user, password):
    if os.path.exists("Data") == False:
        os.mkdir("Data")
    f = open("Data/{}.json".format(user), "r")
    content = f.read()
    content = json.loads(content)
    m = hashlib.md5()
    encoded = password.encode('utf-8')
    m.update(encoded)
    if str(m.digest()) == content["password"]:
        return

    else:
        raise ValueError('Incorrect username or password')
        return

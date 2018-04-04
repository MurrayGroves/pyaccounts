import time
import json
import hashlib
import os

def login():
    user = input("What's your username?\n")
    password = input("What's your password?\n")
    f = open("Data/{}.json".format(user), "r")
    content = f.read()
    content = json.loads(content)
    m = hashlib.md5()
    encoded = password.encode('utf-8')
    m.update(encoded)
    if str(m.digest()) == content["password"]:
        welcome = open("Data/{}.json".format(user), "r").read()
        welcome = json.loads(welcome)
        colour = f = open("Data/{}.json".format(user), "r").read()
        colour = json.loads(colour)
        try:
            colour = colour["colour"]
            print(colour)
            os.system("color {}".format(colour))

        except:
            os.system("color 0F")
        try:
            welcome = welcome["welcome"]
            welcome = welcome.replace("$user$", user)

        except:
            welcome = "Welcome, $user$".replace("$user$", user)
        print(welcome)
        return user
    else:
        print("Incorrect password or username")
        return "error"

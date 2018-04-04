import json
import time
import os
import hashlib

"""Register an account with user defined data"""
def regui():
    if os.path.exists("Data") == False:
        os.mkdir("Data")
    user = input("What do you want your username to be?\n")
    f = open("Data/{}.json".format(user), "w+")
    password = input("What do you want your password to be?\n")
    m = hashlib.md5()
    encoded = password.encode('utf-8')
    m.update(encoded)
    data = {"password": str(m.digest())}
    json.dump(data, f)
    f.close()
    print("Account created")

"""Register an account with software defined data"""
def reg(user, password):
    if os.path.exists("Data") == False:
        os.mkdir("Data")
    m = hashlib.md5()
    encoded = password.encode('utf-8')
    m.update(encoded)
    data = {"password": str(m.digest())}
    f = open("Data/{}.json".format(user), "w+")
    json.dump(data, f)
    f.close()

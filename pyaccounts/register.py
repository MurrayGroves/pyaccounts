import json
import time
import os

try:
    import hashlib
except:
    appdata = os.getenv('LOCALAPPDATA')
    appdata += "/Programs"
    dirs = os.listdirs()
    print(dirs)

def register():
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
    time.sleep(5)

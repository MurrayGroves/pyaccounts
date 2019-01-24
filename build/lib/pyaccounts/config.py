import json
from Crypto.Cipher import AES
import base64

def writeconf(user, password, name, value):
    """Write config data to user file"""
    path = "Data/{}.json".format(user)
    old = json.loads(open(path).read())
    data = {name: value}
    new = {**old, **data}
    f = open(path, 'w')
    json.dump(new, f)
    f.close()
    f = open(path, 'r')

    msg_text = f.read().rjust(32)
    f.close()
    secret_key = password
    if len(secret_key) != 16:
      padding = 'abcdefghijklqwer'
      extra = 16 - len(secret_key)
      add = ''
      for i in range(extra):
        add += padding[i]

      secret_key = secret_key + add

    print(secret_key)
    secret_key = secret_key.encode('utf-8')
    cipher = AES.new(secret_key,AES.MODE_ECB)
    msg_text = msg_text.encode('utf-8')
    encoded = base64.b64encode(cipher.encrypt(msg_text))
    f = open(path, 'w')
    f.write(encoded)
    f.close()

def readconf(user, value):
    """Read config value from user file"""
    path = "Data/{}.json".format(user)
    f = open(path).read()
    decoded = cipher.decrypt(base64.b64decode(f)).strip()

    read = json.loads(decoded)
    try:
      toReturn = read[value]
      return toReturn

    except:
      raise ValueError("Key does not exist")
      return

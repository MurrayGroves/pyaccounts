import time
import json
import hashlib
import os
from Crypto.Cipher import AES
import bcrypt


def pad(toPad):
    """Pad input to be multiple of 16 in length"""

    #Checks if length isn't a multiple of 16
    if (len(toPad) % 16) != 0:
        #Find extra length needed for it to be a multiple of 16
        extra = 16 - (len(toPad) % 16)

        #Generate string long enough to make original string's length a multiple of 16
        add = '|' * extra

        #Adds extra length to original string
        toPad = toPad + add

    #Returns output
    return toPad

def login(user, password):
    """Login to an account with software defined details"""

    secretKeyPadded = pad(password)
    userPadded = pad(user)

    secretKeyPadded = secretKeyPadded.encode('utf-8')
    userPadded = userPadded.encode('utf-8')

    cipher = AES.new(secretKeyPadded,AES.MODE_ECB)

    userEnc = cipher.encrypt(userPadded)
    passwordEnc = cipher.encrypt(secretKeyPadded)

    m = hashlib.sha224()

    m.update(userEnc)

    f = open("Data/{}/{}.data".format(m.hexdigest(),m.hexdigest()),'rb')
    hashedPassword = f.read()

    if bcrypt.checkpw(password.encode('utf-8'), hashedPassword):
        return user,password

    else:
        return 'error','error'

def loginui():
    """Login to an account with user defined details:"""

    username = input("Please input username:\n")
    password = input("Please input password:\n")

    return login(username, password)

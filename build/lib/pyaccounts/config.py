#Import encryption/hashing libraries
from Crypto.Cipher import AES
import hashlib


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

def writeconf(user, password, name, value):
    """Write config data to user file"""

    #Pad values that will be used with crypto as their lengths need to be multiples of 16
    secretKeyPadded = pad(password)
    valuePadded = pad(value)
    userPadded = pad(user)
    namePadded = pad(name)

    #Encode values that will be used with crypto as it only takes bytes
    secretKeyPadded = secretKeyPadded.encode('utf-8')
    valuePadded = valuePadded.encode('utf-8')
    userPadded = userPadded.encode('utf-8')
    namePadded = namePadded.encode('utf-8')

    #Define new AES cipher using user's password as the secret key
    cipher = AES.new(secretKeyPadded,AES.MODE_ECB)

    #Encrypt name and value
    valueEnc = cipher.encrypt(valuePadded)
    userEnc = cipher.encrypt(userPadded)
    nameEnc = cipher.encrypt(namePadded)

    #Create new hashlib sha224 object
    m = hashlib.sha224()
    #Update sha224 object with encrypted username
    m.update(userEnc)

    #Create new hashlib sha224 object
    l = hashlib.sha224()
    #Update sha224 object with encrypted name
    l.update(nameEnc)

    #Write binary data directly to file
    f = open('Data/{}/{}.data'.format(m.hexdigest(),l.hexdigest()),'wb+')
    f.write(valueEnc)
    f.close()

def readconf(user, password, name):
    """Read config value from user file"""

    #Pad password and name as all crypto inputs need to be a multiple of 16 in length
    secretKey = pad(password)
    userPadded = pad(user)
    namePadded = pad(name)

    #Encode value as crypto requires them to be bytes
    secretKey = secretKey.encode('utf-8')
    userPadded = userPadded.encode('utf-8')
    namePadded = namePadded.encode('utf-8')

    #Define new cipher with password as secret key
    cipher = AES.new(secretKey,AES.MODE_ECB)

    #Encrypt username and name
    userEnc = cipher.encrypt(userPadded)
    nameEnc = cipher.encrypt(namePadded)

    #Create new hashlib sha224 object
    m = hashlib.sha224()
    #Update sha224 object with encrypted username
    m.update(userEnc)

    #Create new hashlib sha224 object
    l = hashlib.sha224()
    #Update sha224 object with encrypted name
    l.update(nameEnc)

    #Gets contents of corresponding file
    f = open("Data/{}/{}.data".format(m.hexdigest(),l.hexdigest()),'rb').read()

    #Decrypt file contents
    decrypted = cipher.decrypt(f)

    #Convert bytes to string
    decrypted = decrypted.decode('utf-8')

    #Remove padding from decrypted string
    decrypted = decrypted.replace("|",'')

    #Return information
    return decrypted

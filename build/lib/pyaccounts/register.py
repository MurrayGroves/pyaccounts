#Import miscallaneous modules
import os

#Import encryption modules
import hashlib
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

def reg(user, password):
    """Register an account with software defined data"""

    #Pad user and password because they wil be encrypted and crypto needs them to be a multiple of 16 in length.
    userPadded = pad(user)
    secretKeyPadded = pad(password)

    #Encode user and password because crypto accepts only bytes
    userPadded = userPadded.encode('utf-8')
    secretKeyPadded = secretKeyPadded.encode('utf-8')

    #Create a new cipher object with the user's password as the secret key
    cipher = AES.new(secretKeyPadded,AES.MODE_ECB)

    #Encrypt user and password
    userEnc = cipher.encrypt(userPadded)
    passwordEnc = cipher.encrypt(secretKeyPadded)

    #Create a new hashlib sha224 object
    m = hashlib.sha224()
    #Update sha224 object with encrypted username
    m.update(userEnc)

    #Hash the encrypted password with bcrypt
    hashedPassword = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    #Check if user already exists
    #If user doesn't exist...
    if not os.path.exists("Data/{}".format(m.hexdigest())):
        #Creates folder in data with encrypted and hashed username
        os.makedirs("Data/{}".format(m.hexdigest()))

    #If user exists...
    else:
        #Raise a value error stating that the user already exists to prevent password overriding
        raise ValueError('User already exists')
        #Exit function
        return

    #Create new file in user's folder in binary mode with user's encrypted and hashes username
    f = open('Data/{}/{}.data'.format(m.hexdigest(),m.hexdigest()),'wb+')
    #Write the bytes data of their hashed password directly to the file as binary data
    f.write(hashedPassword)
    #Close the data stream
    f.close()

def regui():
    """Register an account with user defined data"""

    user = input("Please enter username:\n")
    password = input("Please enter password:\n")
    #Call reg with gathered details
    reg(user,password)

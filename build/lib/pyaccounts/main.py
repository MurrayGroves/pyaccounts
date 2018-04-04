from .login import login
from .register import register
#import pyaccounts.config

import time
import json
import os
import hashlib

def main():
    if input("Do you want to register? (Y/N)").lower() == "y":
        register()

        user = login()
        while user == "error":
            user = login()

            while True:
                choice = input("What do you want to do? (login, register, config)")
                if choice == "login":
                    pyaccounts.login()

                elif choice == "register":
                    pyaccounts.register()

                elif choice == "config":
                    pyaccounts.config(user)

                else:
                    print("Invalid Choice")

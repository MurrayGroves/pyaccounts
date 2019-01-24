import login
import register
import config

import time
import json
import os
import hashlib

def main():
    if input("Do you want to register? (Y/N)").lower() == "y":
        register.regui()

    user,password = login.loginui()
    while user == "error":
        user,password = login.loginui()

    while True:
        choice = input("What do you want to do? (login, register, config)")
        if choice == "login":
            login.loginui()

        elif choice == "register":
            register.regui()

        elif choice == "writeconf":
            name = input("name")
            value = input("value")
            config.writeconf(user, password, name, value)

        else:
            print("Invalid Choice")

main()

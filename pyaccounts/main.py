from register import register
from login import login
from config import config
if input("Do you want to register? (Y/N)").lower() == "y":
    register()
user = login()
while user == "error":
    user = login()

while True:
    choice = input("What do you want to do? (login, register, config)")
    if choice == "login":
        login()

    elif choice == "register":
        register()

    elif choice == "config":
        config(user)

    else:
        print("Invalid Choice")

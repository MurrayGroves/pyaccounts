#Import module
import pyaccounts


"""
THIS IS A DEMO FILE

This file is an example of how to use the module

"""


def main():
    #If user wants to register, call registerui
    if input("Do you want to register? (Y/N)").lower() == "y":
        pyaccounts.regui()

    #Get username and password from loginui
    user,password = pyaccounts.loginui()
    #While password or username incorrect; retry
    while user == "error":
        user,password = pyaccounts.loginui()

    #Permanent loop
    while True:
        #Ask user what they want to do
        choice = input("What do you want to do? (login, register, config)")

        #If user wants to login, call loginui
        if choice == "login":
            pyaccounts.loginui()

        #If user wants to register, call regui
        elif choice == "register":
            pyaccounts.regui()

        #If user wants to write a config file, call writeconf with their requested data
        elif choice == "writeconf":
            name = input("name")
            value = input("value")
            pyaccounts.writeconf(user, password, name, value)

        #If user wants to get a config file, call readconf with requested name
        elif choice =="readconf":
            name = input("name")
            print(pyaccounts.readconf(user, password, name))

        #If choice invalid, inform user
        else:
            print("Invalid Choice")

main()

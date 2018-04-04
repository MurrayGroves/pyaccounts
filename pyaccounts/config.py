import time
import json
from login import login

def config(user):
    if user == None:
        user = login()
        while user == "error":
            user = login()

    choice = input("What do you want to change? (welcome message, colour)\n").lower()
    if choice == "welcome message":
        message = input("What do you want your welcome message to be? Use $user$ to put your username or $nick$ for nickname\n")
        content = open("Data/{}.json".format(user), "r").read()
        content = json.loads(content)
        toAdd = {"welcome": message}
        content = {**content, **toAdd}
        f = open("Data/{}.json".format(user), "w")
        json.dump(content, f)
        print("Welcome message changed.\n")

    elif choice == "colour":
        f = open("Data/{}.json".format(user), "r").read()
        content = json.loads(f)
        colour = input("What colour do you want? format like background,text (black, blue, green, purple, white, red, yellow)\n")
        colour = colour.replace(" ", "")
        colour = colour.replace(",", "")
        colour = colour.replace("black", "0")
        colour = colour.replace("green", "A")
        colour = colour.replace("blue", "9")
        colour = colour.replace("purple", "D")
        colour = colour.replace("white", "F")
        colour = colour.replace("red", "C")
        colour = colour.replace("yellow", "E")
        new = {"colour": colour}
        write = {**content, **new}
        f = open("Data/{}.json".format(user), "w")
        json.dump(write, f)
        print("Colour changed")

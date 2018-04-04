import json

"""Write config data to user file"""
def writeconf(user, name, value):
    path = "Data/{}.json".format(user)
    old = json.loads(open(path).read())
    data = {name: value}
    new = {**old, **data}
    f = open(path, 'w')
    json.dump(new, f)
    f.close()

"""Read config value from user file"""
def readconf(user, value):
    path = "Data/{}.json".format(user)
    f = open(path).read()
    read = json.loads(f)
    toReturn = read[value]
    return toReturn

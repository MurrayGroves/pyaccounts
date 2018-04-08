import json

def writeconf(user, name, value):
    """Write config data to user file"""
    path = "Data/{}.json".format(user)
    old = json.loads(open(path).read())
    data = {name: value}
    new = {**old, **data}
    f = open(path, 'w')
    json.dump(new, f)
    f.close()

def readconf(user, value):
    """Read config value from user file"""
    path = "Data/{}.json".format(user)
    f = open(path).read()
    read = json.loads(f)
    toReturn = read[value]
    return toReturn

import os
import time

appdata = os.getenv('LOCALAPPDATA')
appdata += "/Programs/Python/"
os.chdir(appdata)
dirs = os.listdir()
print(type(dirs))
dirs = dirs.sort()

print(type(dirs))
py = dirs[-1]
py = py + "/Scripts/"
print(py)
meme = os.getcwd()
print(meme)
time.sleep(5)

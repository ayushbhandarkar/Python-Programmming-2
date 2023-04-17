# wap to check whether it is file or folder

import os

path = "D:\\notes & Projects\\python\\practice programs\\File1.txt"

if os.path.isfile(path):
    print(" It is an file :) ")
elif os.path.isdir(path):
    print(" It is an Folder/ directory :) ")
else:
    print(" File/folder is not present at specified location :( ")


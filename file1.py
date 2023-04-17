# wap to check the file is available in the system or not

import os

path = "D:\\notes & Projects\\python\\new_programs\\basic concepts\\ New file.txt"

if os.path.exists(path):
    print(" File found ! You can read data from file")
else:
    print(" File not found")

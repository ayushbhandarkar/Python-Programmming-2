# Reading more than one line from file : File1.txt

ptr = open("File1.txt", "r")
num = int(input(" Enter number of lines to read : "))

for i in range(num):
    print(ptr.readline(), end=" ")
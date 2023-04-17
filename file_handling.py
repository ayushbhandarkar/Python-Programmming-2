f = open("file_handling.docx", "r")

# data = input(" Enter anything : ")
# f.write(" This is an demo lecture to understand file handling (write mode) \n"+data)

# data = f.read(5)  # this will read perticular 5 char.

data = f.readline()
print(data)

f.close()

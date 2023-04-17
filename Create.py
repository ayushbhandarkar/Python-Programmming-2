fp = open("File1.txt", "a")         # "a" this will merge new data with previous data
data = input(" Enter some new data : ")
fp.write(data)

# wap to convert tuple into list

Array1 = ("data1", 10, 20, 30, 40, "data2")     # data is in tuple
print(type(Array1), Array1)

Array2 = list(Array1)           # type conversion - tuple into list
print(type(Array2), Array2)

Array2.insert(2, 100)
print(type(Array2), Array2)

Array1 = tuple(Array2)          # type conversion - list into tuple
print(type(Array1), Array1)


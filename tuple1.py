# wap to change the type of collection tuple-list-tuple

Tuple = (1, 'a', True, 3.14, 5)
print(Tuple)

print("Before changing type : ", type(Tuple))
Tuple = list(Tuple)            # changing type
print("After changing type : ", type(Tuple))

Tuple.clear()
print(Tuple)

Tuple = tuple(Tuple)
print("After changing type again : ", type(Tuple))
dict = {"Rice": 30,
        "wheat": 27,
        "oil": 50,
        "Rice": 20}

print(dict)
# print(type(dict))
# print(" Length of dictionary : ", len(dict))
# data = dict.get("oil")
# data = dict.keys()
# data = dict.values()
# data = dict.items()
# print(data)

dict.update({"sugar": 30})
print(" After updating : ", dict)
# poped = dict.pop("sugar")
# print("Poped item : ", poped)

# del dict["sugar"]
# print(dict)

# data = dict.popitem()
# print(data)

# del dict

# dict.clear()
# print(dict)

dict2 = dict.copy()
print("dict2 : ", dict2)
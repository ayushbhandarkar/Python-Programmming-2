def swap(ls):
	first=ls.pop(0)
	last=ls.pop(-1)
	ls.insert(0,last)
	ls.append(first)
	print(ls)

ls=[1,2,3,4,5]
swap(ls)
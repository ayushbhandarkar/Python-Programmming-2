def max(ls):
	a=ls[0]
	for i in ls:
		if a<i:
			a=i
	return a




ls=[3,4,1,6,2]
big=max(ls)
print(f"{big} is the largest number ")
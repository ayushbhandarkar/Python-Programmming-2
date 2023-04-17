def max(ls):
	i=0
	max1=ls[0]
	while i<len(ls):
		if max1<ls[i]:
			max1=ls[i]
		i=i+1
	return max1



ls=[3,4,1,6,2]
big=max(ls)
print(f"{big} is the largest number ")
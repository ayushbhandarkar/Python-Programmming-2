
def add(ele):
	i=0
	sum=0
	while i<len(ele):
		sum=sum+ele[i]
		i=i+1
	return sum

ele=[2,4,3,5,6]
total=add(ele)
print(total)
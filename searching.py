'''def search(ls):
	ele=int(input(" Enter the element to search "))
	for i in ls:
		if ele==i:
			print(" The element is found ")
			break


ls=[1,2,4,3,5]
search(ls)
'''

def search(ls):
	ele=int(input(" Enter the element to search "))
	i=0
	while i<len(ls):
		if ele==ls[i]:
			print(f" The element {ele} is found at {i+1} position")
			break
		i=i+1


ls=[1,2,4,3,5]
search(ls)
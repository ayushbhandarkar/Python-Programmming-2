num=int(input(" Enter the number : "))
n1=0
n2=1

if num <= 0:
	print(" Its invalid number")
elif num==1:
	print(n1)
else:
	i=0
	while i<num:
		print(n1)
		nth=n1+n2
		n1=n2
		n2=nth
		i=i+1
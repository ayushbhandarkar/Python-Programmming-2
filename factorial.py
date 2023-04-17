def fact(num):
	factorial=1
	i=1
	while i<=num:
		factorial*=i
		i=i+1
	print(f" The factorial of {num} = {factorial}")

num=int(input(" Enter the number : "))
fact(num)
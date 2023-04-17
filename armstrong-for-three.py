num=int(input(" Enter the three digit number : "))
num1=num
sum=0
while num1>0:
	digit=num1%10
	sum+=digit**3
	num1//=10
if num==sum:
	print(f" The number {num} is an armstrong number")
else:
	print(f" The number {num} is not armstrong number")
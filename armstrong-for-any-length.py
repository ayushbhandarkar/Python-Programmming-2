num=input(" Enter any random number of any length ")
num1=int(num)
sum=0
count=len(num)
while num1!=0:
	digit=num1%10
	sum+=digit**count
	num1//=10
if num==sum:
	print(f" The number {num} is an armstrong number")
else:
	print(f" The number {num} is not armstrong number")
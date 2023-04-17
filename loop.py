"""                                     For loop 

#1
print('\t\t\t Program to print factors of a number ')
n=int (input(' Enter the number till to print factors :'))
for i in range(1,n+1,1):
    print(i)

#2
print('\t\t\t Program to print sum of a number ')
n=int (input(' Enter the number :'))
sum=0
for i in range(1,n+1,1):
    sum+=i
    print( i)
print('Sum of number :',sum)

#3
print('\t\t\t Program to print Factorial of a number ')
n=int (input(' Enter the number :'))
fact=1
for i in range(1,n+1,1):
    fact*=i
    print(i)
print('Factorial of number :',fact)

#4
print('\t\t\t Program to check the alphabet is vowel or consonant')
ch= (input(' Enter the alphabet :'))
for i in ch:
    if i=='a'or i=='A' or i=='e'or i=='E' or i=='i'or i=='I' or i=='o'or i=='O' or i=='u'or i=='U':
        print(' The alphabet is vowel')
    else:
        print(' The alphabet is consonant')

#5
print(' Program to check the number is prime or not ')
n=int (input(' Enter the number :'))
for i in range(2,n,1):
    if  n%i==0:
        print(' The number is not prime')
        break
if n==i+1:
    print(' The number is prime')

#6
print(' Program to print prime numbers between 1 to 50 ')
for n in range(1,51,1):
    f=1
    for i in range(2,n,1):
        if  n%i==0:
            f=0
            break
    if f==1:
        print(n)

#7
print(' wap to print all the numbers within the user range which is divisible by user input :')
f=int (input(' Enter the first number of range :'))
l=int (input(' Enter the last number of range :'))
num=int (input(' Enter the number to divide :'))
for i in range(f,l+1,1):
    if i%num==0:
        print(i)

#8
print(' wap to print fibonacci series')
f1=0
f2=1
n=int (input(' Enter the number'))
print(f1,f2,sep="  ",end="  ")
for i in range (3,n,1):
    f3=f1+f2
    f1=f2
    f2=f3
    print(f3,sep="  ",end="  ")

#9
# patttern program 1
for row in range (1,6,1):
    for col in range (1,6,1):
        print(" *",sep=" ",end=" ")
    print(" ")
    
#10
# patttern program 2
for row in range (1,6,1):
    for col in range (1,6,1):
        print(row,sep=" ",end=" ")
    print(" ")
    
#11
# patttern program 3
for row in range (1,6,1):
    for col in range (1,6,1):
        print(col,sep=" ",end=" ")
    print(" ")
    
#12
# patttern program 4
i=1
for row in range (1,6,1):
    for col in range (1,6,1):
        print(i,sep=" ",end=" ")
        i+=1
    print(" ")
    
#13
# patttern program 5
for row in range (1,6,1):
    for col in range (1,row+1,1):
        print(row,sep=" ",end=" ")
    print(" ")
   
#14
# patttern program 6
for row in range (1,6,1):
    for col in range (1,row+1,1):
        print(col,sep=" ",end=" ")
    print(" ")
 
#15
# Floyd's triangle 
i=1
for row in range (1,6,1):
    for col in range (1,row+1,1):
        print(i,sep=" ",end=" ")
        i+=1
    print(" ")
    
#16
# Pyramid
n= int(input( 'Enter the number or rows :'))
i=n
for row in range (1,n+1,1):
    for sp in range (1,i,1):
        print(sep=" ",end=" ")
    i-=1
    for st in range (1,row+1,1):
        print("*",sep=" ",end=" ")
    print()
    
#17
# Inverse Pyramid
n= int(input( 'Enter the number or rows :'))
i=n
for row in range (1,n+1,1):
    for sp in range (1,row,1):
        print(sep=" ",end=" ")
    for st in range (1,i+1,1):
        print("*",sep=" ",end=" ")
    i-=1
    print()
    
#18
# Diamond
n= int(input('Enter the number or rows :'))
i=n
for row in range (1,n,1):
    for sp in range (1,i,1):
        print(sep=" ",end=" ")
    i-=1
    for st in range (1,row+1,1):
        print("*",sep=" ",end=" ")
    print()
i=n
for row in range (1,n+1,1):
    for sp in range (1,row,1):
        print(sep=" ",end=" ")
    for st in range (1,i+1,1):
        print("*",sep=" ",end=" ")
    i-=1
    print()
    

#19
# Kite
n= int(input('Enter the number or rows :'))
i=n
for row in range (1,n,1):
    for sp in range (1,i,1):
        print(sep=" ",end=" ")
    i-=1
    for st in range (1,row+1,1):
        print("*",sep=" ",end=" ")
    print()
i=n
for row in range (1,n+1,1):
    for sp in range (1,row,1):
        print(sep=" ",end=" ")
    for st in range (1,i+1,1):
        print("*",sep=" ",end=" ")
    i-=1
    print()
for row in range (1,4,1):
    for sp in range (row,n,1):
        print(sep=" ",end=" ")
    for st in range (1,row+1,1):
        print("*",sep=" ",end=" ")
    print()

#20
# pattern program 7
for r in range (5):
    for c in range (5):
      if (r+c==2 or c-r==2 or r-c==2 or r+c==6):
          print("*",end=" ")
      else:
          print(end=" ")
    print();

#21
# wap to print sum of factors of a number
n= int (input(' Enter the number :'))
sum=0
while(n>0):
    d=n%10
    sum=sum+d
    n=n//10
print(sum)

#22
# wap to print Reverse of a number
n= int (input(' Enter the number :'))
rev=0
while(n>0):
    d=n%10
    rev=rev*10+d
    n=n//10
print(rev)


#23
# wap to print the number is pallindrom or not
n= int (input(' Enter the number :'))
org=n
rev=0
while(n>0):
    d=n%10
    rev=rev*10+d
    n=n//10
print(' Reverse :',rev)
if(rev==org):
    print(' The number is pallindrom')
else:
    print(' The number is not pallindrom ')


#24
#wap to print the number is armstrong or not
n=int (input(' Enter the number :'))
org=n
sum=0
while(n>0):
    d=n%10
    sum=sum+d*d*d
    n=n/10
print(' Cubic addition :',sum)
if(org==sum):
    print(' The number is armstrong')
else:
    print(' The number is not armstrong')
"""














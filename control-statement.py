"""                           Control statement """



"""                           if statement

print('\t\t\t wap to print absolute number ')
n=int (input(' Enter the number :'))
if n<0: n*=-1
print(' Absolute number :',n)
"""

"""                           if-else statement 

print('\t\t\t wap to check the number is positive or negetive')
n=int (input('Enter the number :'))
if n>0: print(' The number is positive')
else: print('The number is negetive')


print('\t\t\t wap to check the student is pass or fail ')
s1=float (input('Enter the first subject marks :'))
s2=float (input('Enter the second subject marks :'))
s3=float (input('Enter the third subject marks :'))
s4=float (input('Enter the fourth subject marks :'))
s5=float (input('Enter the fifth subject marks :'))
total=s1+s2+s3+s4+s5
avg=total/5
print(' Sum of five sub. marks :',total)
print(' Percentage :',avg)
if avg>40: print(' The student is pass')
else: print(' The student is fail')


print(' program to check the alphabet is vowel or consonant using or operator ')
char= input(' Enter the alphabet :')
if char=='a'or char=='e'or char=='i'or char=='o'or char=='u': print(' The alphabet is vowel')
else:print(' The alphabet is consonant')
"""

"""                             if-elif-else statement 

print(' Program to check the number is positive negetive or zero')
n=int (input('Enter the number :'))
if n>0: print(' The number is positive ')
elif n<0: print(' The number is negetive')
else: print(' The number is zero')


print(' program to check the alphabet is vowel or consonant ')
char= input(' Enter the alphabet :')
if char=='a'or char=='A': print(' The alphabet is vowel')
elif char=='e'or char=='E':print(' The alphabet is vowel')
elif char=='i'or char=='I':print(' The alphabet is vowel')
elif char=='o'or char=='O':print(' The alphabet is vowel')
elif char=='u'or char=='U':print(' The alphabet is vowel')
else:print(' The alphabet is consonant')


print('Program to check the biggest between four variable ')
a=int (input(' Enter the value of a,b,c,d :'))
b=int (input())
c=int (input())
d=int (input())
if a>b and a>c and a>d: print(' A is greater ')
elif b>a and b>c and b>d: print(' B is greater ')
elif c>a and c>b and c>d: print(' C is greater ')
elif d>a and d>b and d>c: print(' D is greater ')
else:print(' Both the four numbers are same')


print(' Program to check whether the entered character is number, alphabet or special character ')
ch= (input(' Enter the character :'))
if ch>='a'and ch<='z'or ch>='A'and ch<='Z':print(' The character is an alphabet ')
elif ch>='1' and ch<='9':print(' The character is number ')
else: print(' It is a special character ')
"""

"""                             nested if statement 

print(' Program to check the biggest between four numbers ')
a=int (input(' Enter the value of a :'))
b=int (input(' Enter the value of b :'))
c=int (input(' Enter the value of c :'))
d=int (input(' Enter the value of d :'))
if a>b:
    if a>c:
        if a>d: print(' A is biggest ')
        else:print(' D is biggest ')
    elif c>d:print(' C is biggest')
    else:print(' D is biggest')
elif b>c:
    if(b>d):print(' B is biggest')
    else:print(' D is biggest')
elif c>d:print(' C is biggest')
else:print(' D is biggest')


print(' Program to print check for valid date')
dd=int (input(' Enter the date :'))
mm=int (input(' Enter the month :'))
yy=int (input(' Enter the year :'))
if yy>=1900 and yy<=9999:
    if mm>=1 and mm<=12:
        if dd>=1 and dd<=31 and mm==1 or mm==3 or mm==7 or mm==8 or mm==10 or mm==12:
            print(' It is a valid date from month of 31 days ')
        elif dd>=1 and dd<=30 and mm==4 or mm==6 or mm==9 or mm==11:
            print(' It is a valid date from month of 30 days ')
        elif dd>=1 and dd<=28 or dd<=29 and mm==2:
            print(' It is a valid date from February month')
        else:print(' Invalid Date')
    else:print(' Invalid month !')
else:print(' Invalid Year !')
"""






































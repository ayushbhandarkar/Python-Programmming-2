name=input(" Enter the name : ")
i=0
while i<len(name)/2:
	if name[i]==name[-i-1]:
		i+=1
	else:
		break
if i>len(name)/2:
	print(" The name is pallindrom")
else:
	print(" The name is not pallindrom")
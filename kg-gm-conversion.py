'''kg=int(input("Enter the weight in kg "))
gm=kg*1000
print(f"{kg} ={gm} gm")'''

def kg_to_gm(kg):	#function definition
	gm=kg*1000
	return gm

kg=int(input("Enter the weight in kg "))
gms=kg_to_gm(kg)

print(f"{kg} ={gms} gms")
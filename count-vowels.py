vowel="aeiou"
str="Hello,I am Python"
str=str.casefold()		 # for caseless comparion
count={}.fromkeys(vowel,0)	# dictonary function

for ch in str:
	if ch in count:
		count[ch]+=1

print(count)
vowel,flag=['a','e','i','o','u','A','E','I','O','U'],0
s=input("Enter a string: ")
for char in s:
    if char in vowel:
        flag=1
        break
if flag==1:
    print(s,"Contains at least one vowel.")
else:
    print(s,"Does not contain any vowel.")
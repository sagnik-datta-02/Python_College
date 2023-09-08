s=input("Enter a string: ")
s1,s2="",""
for char in s:
    if char.islower():
        s1+=char
    else:
        s2+=char
print("Modified string: ",s1+s2)
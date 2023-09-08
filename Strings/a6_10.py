s1=input("Enter the first string: ")
s2=input("Enter the second string: ")
l=len(s1)
print("Modified string: ", s1[slice(0,l//2,1)]+s2+s1[slice(l//2,l,1)])
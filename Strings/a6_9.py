s=input("Enter a string: ")
l=len(s)
print("Modified string: ",s[slice(l//2-1, l//2+2, 1)])
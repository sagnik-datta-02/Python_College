s=input("Enter a string: ")
l=len(s)
if l%2!=0 and l>1:
    print("Modified string: ",s[0]+s[l//2]+s[l-1])
elif l%2==0 and l>2:
    print("Modified string: ",s[0],s[(l//2)-1]+s[(l//2)]+s[l-1])
elif l==1 or l==2:
    print("modified string: ",s)
s1=input("Enter  first string: ")
s2=input("Enter second string: ")
flag=0
for ch in s2:
    for ch1 in s1:
        if ch==ch1:
            flag=1
if flag==1:
    print("True")
else:
    print("False")
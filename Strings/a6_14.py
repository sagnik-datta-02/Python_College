s1=input("Enter a string: ")
s2=input("Enter a string: ")
l1,l2,i,j,s3=len(s1),len(s2),0,-1,""
while i<l1 and j>=-l2:
    if i<l1:
        s3+=s1[i]
    if j>=-l2:
        s3+=s2[j]
if i<=l1:
    s3+=s1[slice(i,l1,1)]
if j>=-l2:
    s3+=s2[slice(j,-l2-1,-1)]
print("Modified string: ",s3)
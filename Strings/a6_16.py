s=input("Enter a string: ")
sub=input("Enter the substring whose occurance is to be found: ")
count,s,s1=0,s+"",""
for i in range(0,len(s)):
    if s[i]!=" " and s[i]!="?" and s[i]!="." and s[i]!=",":
        s1+=s[i]
    else:
        if sub.lower()==s1.lower():
            count+=1
        s1=""
print("The",sub,"count: ",count)
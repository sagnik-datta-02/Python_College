s=input("Enter a string: ")
count,s,s1=0,s+"",""
for i in range(0,len(s)):
    if s[i]!=" " and s[i]!="?" and s[i]!="." and s[i]!=",":
        s1+=s[i]
    else:
        for ch in s1:
            if ch.isdigit():
                print(s1)
                break
        s1=""
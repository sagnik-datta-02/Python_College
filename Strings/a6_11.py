n=int(input("enter the number of strings: "))
lst,s1,s2,s3 = [],"","",""
print("Enter the strings: ")
for i in range(0,n):
    str=input()
    lst.append(str)
for i in range(0,n):
    s1+=lst[i][0]
    s2+=lst[i][len(lst[i])//2]
    s3+=lst[i][len(lst[i])-1]
print("Modified string: ",s1+s2+s3)
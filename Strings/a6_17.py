s=input("Enter a string: ")
sum,avg,count=0,0,0
for char in s:
    if char.isdigit():
        sum+=int(char)
        count+=1
avg=sum/count
print("Sum is: ",sum,"Average is: ",avg)
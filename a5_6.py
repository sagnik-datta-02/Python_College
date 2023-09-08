n=int(input("Enter a number: "))
s=0
for i in range(1,n+1):
    s+=(i**2)/i
print("Sum of series: ",s)
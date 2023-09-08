n=int(input("Enter a number: "))
s=0
for i in range(1, n+1):
    s+=1/(i**2)
    print("Sum of series: ",s)
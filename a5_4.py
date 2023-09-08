n=int(input("Enter a number: "))
f=0
for i in range(1,n+1):
    if n%i==0:
        f+=1
if f==2:
    print(i,"is a Prime Number")
else:
    print(i,"is a Composite Number")
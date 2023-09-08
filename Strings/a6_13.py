s=input("Enter a string: ")
ca,cd,cs=0,0,0
for char in s:
    if char.isalpha():
        ca+=1
    elif char.isdigit():
        cd+=1
    else:
        cs+=1
print("Total count of alphabets, digits and special symbols: ")
print("Alphabets: ",ca)
print("Digits: ",cd)
print("Special symbols: ",cs)
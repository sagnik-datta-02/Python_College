s=input("Enter a string: ")
for ch in s:
    if ch.isalpha()==False and ch.isdigit()==False and ord(ch)!=32:
        s=s.replace(ch,"")
print(s)
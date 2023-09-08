s=input("Enter a string: ")
for ch in s:
    if ch.isalpha() or ord(ch)==32:
        s=s.replace(ch,"")
print(s)
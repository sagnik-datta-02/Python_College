n=int(input("Enter the number of strings in the list: "))
lst=[]
print("Enter the elements of the list: ")
for i in range(0,n):
    ele=input()
    lst.append(ele)
print("Original list of strings: ")
print(lst)
while '' in lst:
    lst.remove('')
print("After removing empty strings: ")
print(lst)
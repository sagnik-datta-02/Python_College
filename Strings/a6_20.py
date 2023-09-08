def find_last_position(main_string, substring):
    last_position=main_string.rfind(substring)
    return last_position
main_string=input("Enter the main string: ")
substring=input("Enter the substring to find: ")
last_position=find_last_position(main_string, substring)
if last_position!=-1:
    print("Last occurance of",substring,"starts at index",last_position)
else:
    print(substring,"was not found in the main string")
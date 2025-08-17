# 19. Write a Python program to get the last part of a string before a specified character.
# https://www.w3resource.com/python-exercises
# https://www.w3resource.com/python

string = input("Enter the string: ")
character = input("Enter the character: ")
part = string.split(character)
if len(part) > 1:
    result = part[-2] #lấy phần tử trước phần tử cuối cùng
else: result = string
print("The last past of a string before a specific character is: ",result)

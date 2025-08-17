# 24. Write a Python program to check whether a string starts with specified characters
string = input('Enter a string: ')
prefix = input("Enter character or string starts need to check: ")
if string.startswith(prefix):
    print("String starts with: ", prefix)
else:
    print("String don't start with: ", prefix)
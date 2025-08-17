# 47. Write a Python program to lowercase the first n characters in a string
string=input("Enter the string:")
n=int(input("Enter the number: "))
result = string[:n].lower() + string[n:]
print(result)
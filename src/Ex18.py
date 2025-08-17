# 18. Write a Python function to get a string made of the first three characters of a specified string.
# If the length of the string is less than 3, return the original string.
# Sample function and result :
# first_three('ipy') -> ipy
# first_three(' python') -> pyt
string = input("Enter the string: ")
if len(string) <= 3:
    result = string
else:
    result= string[:3]
print("Result is: ",result)
# 5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz

print("Cách 1: ", end="")
string1 = input("Enter the string one: ")
string2 = input("Enter the string two: ")
string1_new = string2[:2] + string1[2:]
string2_new = string1[:2] + string2[2:]
print(string1_new, end=" ")
print(string2_new)

print("Cách 2: ", end="")
string1 = input("Enter the string one: ")
string2 = input("Enter the string two: ")
string1_new = string2[:2] + string1[2:]
string2_new = string1[:2] + string2[2:]
result = string1_new + " " + string2_new
print(result)
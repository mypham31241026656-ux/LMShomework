# 3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String
from queue import Empty
#Thử
string = "w3resource"
print(string[0:2], end="")
print(string[-2::])
#Cách 1
print("Cách 1: ", end="")
string = input("Enter a string: ")
if(len(string) < 2):
    print("Empty String")
else:
    print(string[0:2], end="")
    print(string[-2::])
#Cách 2
print("Cách 2: ", end="")
string = input("Enter a string: ")
if(len(string) < 2):
    print("Empty String")
else:
    result = string[0:2]+string[-2::]
    print(result)
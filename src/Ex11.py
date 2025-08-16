# 11. Write a Python program to remove characters that have odd index values in a given string
string = input("Enter the string: ")
result = ""
for i in range(len(string)):
    if i % 2 == 0:
        result += string[i]
print("Result is:", result)
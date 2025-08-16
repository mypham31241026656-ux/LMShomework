# 9. Write a Python program to remove the nth index character from a nonempty string.
string = input("Enter a string: ")
n = int(input("Enter the nth index character need to remove (start with 0): "))
result = string[:n]+string[n+1:]
print("Result is:", result)
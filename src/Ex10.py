# 10. Write a Python program to change a given string to a newly string where the first and last
# chars have been exchanged
string = input("Enter a string: ")
if len(string) > 1:
    result = string[-1] + string[1:-1]+string[0]
else: result = string
print("Result is:", result)
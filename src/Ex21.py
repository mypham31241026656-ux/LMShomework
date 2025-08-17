# 21. Write a Python function to convert a given string to all uppercase if it contains at least 2
# uppercase characters in the first 4 characters.
string = input("Enter a string: ")
first_four = string[:4]

count_upper = 0
for char in first_four:
    if char.isupper():
        count_upper += 1
if count_upper >= 2:
    result = string.upper()
else:
    result = string
print("Result is: ",result)
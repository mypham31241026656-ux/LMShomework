# 48. Write a Python program to swap commas and dots in a string.
# Sample string: "32.054,23"
# Expected Output: "32,054.23"
string = "32.054,23"
temp = string.replace('.', 'temp')
temp = temp.replace(',', '.')
result = temp.replace('temp', ',')
print(result)

# 44. Write a Python program to print the index of a character in a string.
# Sample string: w3resource
# Expected output:
# Current character w position at 0
# Current character 3 position at 1
# Current character r position at 2
# - - - - - - - - - - - - - - - - - - - - - - - - -
# Current character c position at 8
# Current character e position at 9
string = 'w3resource'
for index, character in enumerate(string): #lấy vị trí (index) của từng ký tự trong chuỗi
    print(f"Current character '{character}' is: {index}")
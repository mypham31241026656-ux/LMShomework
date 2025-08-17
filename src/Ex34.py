# 34. Write a Python program to print the following integers with '*' to the right of the specified
# width
numbers=[5,9,7,11]
width = 8
for number in numbers:
    print(f"{number:*<{width}d}") # '*' điền bên phải (căn trái)
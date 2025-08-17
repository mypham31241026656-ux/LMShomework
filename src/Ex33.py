# 33. Write a Python program to print the following integers with zeros to the left of the specified
# width
numbers = [9, 18, 19, 8, 20006]
width = 10
for number in numbers:
    print(f"{number:0{width}d}") #decimal integer
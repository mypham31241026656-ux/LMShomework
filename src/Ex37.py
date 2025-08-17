# 37. Write a Python program to display a number in left, right, and center aligned with a width of 10.
number = 90
width = 10
print(f"{number:>{width}}")
print(f"{number:<{width}}")
print(f"{number:^{width}}")

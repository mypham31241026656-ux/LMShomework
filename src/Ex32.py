# 32. Write a Python program to print the following positive and negative numbers with no
# decimal places.
numbers = [3.14159, 2.17165, -2.5]
for number in numbers:
    print(f"{number:+.0f}")
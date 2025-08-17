# 31. Write a Python program to print the following numbers up to 2 decimal places with a sign
numbers = [3.14159, 2.71828, -0.4]
for number in numbers:
    print(f"{number:+.2f}")
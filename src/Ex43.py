# 43. Write a Python program to print the square and cube symbols in the area of a rectangle and
# the volume of a cylinder.
# Sample output:
# The area of the rectangle is 1256.66cm2
# The volume of the cylinder is 1254.725cm3
import math

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
radius = int(input("Enter the radius of the cyclinder: "))
height = int(input("Enter the height of the cyclinder: "))
area_rectangle = length * width
volume_cyclinder = math.pi * pow(radius, 2)*height
print(f"The area of the rectangle is: {area_rectangle}cm\u00b2")
print(f"The volume of the cyclinder is: {volume_cyclinder}cm\u00b3")

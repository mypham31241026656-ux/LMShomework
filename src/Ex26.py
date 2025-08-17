# 26. Write a Python program to display formatted text (width=50) as output
import textwrap

text = "Python is a powerful programming language that lets you work quickly and integrate systems more effectively "
formatted_text = textwrap.fill(text, width=50)
print(formatted_text)

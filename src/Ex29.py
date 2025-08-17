# 29. Write a Python program to set the indentation of the first line.
text = '''Python is easy to learn.
It is widely used.
Learning Python is fun.'''
indent = "    "
lines = text.split("\n")
lines[0] = indent + lines[0]
new_text = "\n".join(lines)
print(new_text)
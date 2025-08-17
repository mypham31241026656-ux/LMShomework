# 28. Write a Python program to add prefix text to all of the lines in a string.
text = (''' Python is a powerful programming language 
        That lets you work quickly 
        Integrate systems more effectively''')
prefex = ">>>"
new_text = ""
for line in text.split("\n"):
    new_text += prefex+ line + "\n"
print(new_text)
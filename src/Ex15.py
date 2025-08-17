# 15. Write a Python function to create an HTML string with tags around the word(s).
# Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutor")-> '<b>Python Tutorial </b>'
tag = input("Enter the tags: ")
text = input("Enter the text: ")
html_string = "<" + tag + ">" + text + "</" + tag + ">"
print(html_string)
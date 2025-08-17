#41. Write a Python program to strip a set of characters from a string.
string = " **//Hello World This Is My World===+++"
char_to_strip = "*/=+"
for c in char_to_strip:
    string = string.replace( c,"")
print(string)
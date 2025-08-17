# 40. Write a Python program to reverse words in a string.
string = input("Enter a string: ")
words = string.split()
words.reverse()
reversed_string = " ".join(words)
print(reversed_string)
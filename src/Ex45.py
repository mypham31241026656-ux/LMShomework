# 45. Write a Python program to check whether a string contains all letters of the alphabet
string_to_check = "The quick brown fox jumps over the lazy dog"
string_lower = string_to_check.lower()
alphabet_set = set('abcdefghijklmnopqrstuvwxyz')
string_set = set(string_lower)
if alphabet_set.issubset(string_set):
    print("The string contains all letters of the alphabet.")
else:
    print("The string does not contain all letters of the alphabet.")
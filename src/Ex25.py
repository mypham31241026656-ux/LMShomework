# 25. Write a Python program to create a Caesar encryption.
# Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's
# code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a
# type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed
# number of positions down the alphabet. For example, with a left shift of 3, D would be replaced
# by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his
# private correspondence.
string = input("Enter the string need to ecript: ")
shift = int(input("Enter the shift number: "))
cipher_string = ""
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
#X là vị trí 23 (0-based: A=0, B=1, … Z=25)
# #X + 3 = 26 → 26 % 26 = 0 → A
# Y + 3 = 27 → 27 % 26 = 1 → B
# Z + 3 = 28 → 28 % 26 = 2 → C
for char in string:
    if char.isupper(): #Nếu là chữ hoa → tìm vị trí trong bảng chữ hoa
        index = alphabet.index(char)
        new_index = (index + shift) % 26
        cipher_string += alphabet[new_index]
    elif char.islower():
        index = alphabet_lower.index(char)
        new_index = (index + shift) % 26
        cipher_string += alphabet_lower[new_index]
    else:
        cipher_string += char #giữ nguyên ký tự khác
print(cipher_string)


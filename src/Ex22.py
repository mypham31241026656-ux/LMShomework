# 22.Write a Python program to sort a string lexicographically.
string = input("Enter a string: ")
result = ''.join(sorted(string)) # sorted() trả về list các ký tự, dùng join để thành chuỗi
print("A string lexicographically: ",result)

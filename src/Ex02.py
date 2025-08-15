# 2. Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
from itertools import count

string = "google.com"
print("Cách 1: ", end="")
for characters in set(string):
    print(f"'{characters}': {string.count(characters)}") #Hàm .count() đếm số lần ký tự xuất hiện trong toàn bộ chuỗi

string = "google.com"
result = {} # Dictionary rỗng
print("Cách 2: ", end="")
for characters in string: #Duyệt qua từng ký tự trong chuỗi, theo thứ tự gốc: Lý do: Nếu đã đếm rồi, không cần đếm lại nữa → giữ đúng thứ tự lần đầu gặp.
    if characters not in result: # Nếu ký tự chưa có trong dictionary (result), thì mới đếm.
        result[characters] = string.count(characters) # Đếm tổng số lần ký tự xuất hiện trong chuỗi.
#gán giá trị cho characters trong dictionary ket_qua.
print(result)
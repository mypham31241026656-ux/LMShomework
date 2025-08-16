# 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'
string = input("Enter a string: ")
result = ""  # Chuỗi kết quả (ban đầu rỗng)
ky_tu_dau = ""  # Nơi để nhớ ký tự đầu tiên
landau = True  # Đánh dấu ký tự đầu tiên

for char in string:
    if landau:
        ky_tu_dau = char  # Lưu ký tự đầu
        result += char  # Thêm nó vào kết quả
        landau = False  # Không phải lần đầu nữa
    else:
        if ky_tu_dau == char:
            result += "$"  # Nếu trùng ký tự đầu thì thay $
        else:
            result += char  # Nếu khác thì giữ nguyên
print(result)

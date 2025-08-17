# 27. Write a Python program to remove existing indentation from all of the lines in a given text.
text = '''Python is a powerful programming language.
            That lets you work quickly .
  Integrate systems more effectively.'''

lines = text.split("\n") #Tách các dòng
new_lines = [line.strip() for line in lines] #Xóa khoảng trắng đầu dòng
new_text = "\n".join(new_lines) #Ghép lại thành chuỗi
print(new_text)
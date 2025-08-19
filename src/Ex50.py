# 50. Write a Python program to split a string on the last occurrence of the delimiter.
#Viết chương trình Python tách chuỗi theo lần xuất hiện cuối cùng của ký tự phân tách
text = input("Enter the text: ")
delimeter = input("Enter the delimeter: ")
part = text.rsplit(delimeter,1)
print(part)

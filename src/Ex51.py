# 51. Write a Python program to find the first non-repeating character in a given string
#Viết chương trình Python để tìm ký tự xuất hiện đầu tiên mà không bị lặp lại trong một chuỗi.
string = input("Enter a string: ")
for char in string:
    if string.count(char) == 1:
        print("Kí tụ xuất hiện đầu tiên mà không bị lặp lại trong chuỗi là: ",char )
        break #thoát khỏi vòng lặp ngay
else: print("Không có kí tự nào thỏa mãn")
# 14. Write a Python program that accepts a comma-separated sequence of words as input and
# prints the distinct words in sorted form (alphanumerically).
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white,red
words = input("Enter comma-separated words: ")
words_list = words.split(',') #Nếu loại bỏ khoảng trắng thì lệnh [word.strip() for word in words.split(",")]
distinct_words = sorted(set(words_list))
for i in range(len(distinct_words)):
    if i == len(distinct_words) - 1:  #NẾu là phần tử cuối cùng
        print(distinct_words[i])
    else:
        print(distinct_words[i], end=",") #Còn lại thì thêm dấu phẩy sau từ
        #end="," nghĩa là không xuống dòng mà in thêm dấu phẩy sau mỗi từ


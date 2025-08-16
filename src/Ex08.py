# 8. Write a Python function that takes a list of words and return the longest word and the length of the longest one.
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9

words = input("Enter the words: ").split()  # cách nhau bởi dấu cách
longest_word = ""  # ban đầu rỗng
for word in words:  # Duyệt qua từng từ trong các từ
    if len(word) > len(longest_word):
        longest_word = word
print("Longest word is:", longest_word)
print("Length of longest word is:", len(longest_word))

# 12. Write a Python program to count the occurrences of each word in a given sentence

sentence = input("Enter the sentence: ")
words = sentence.split()
for word in words:
    count = words.count(word)
    print(word, ":", count)

sentence = input("Enter the sentence: ")
words = sentence.split()
count = {}
for word in words:
    if word in count: count[word] += 1
    else: count[word] = 1
print(count)
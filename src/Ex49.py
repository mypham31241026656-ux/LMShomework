# 49. Write a Python program to count and display vowels in text
# Viết chương trình Python đếm và hiển thị các nguyên âm trong đoạn văn bản.
text = input("Enter a text: ")
vowel = "aeiouAEIOU"
counts = {}
for char in text:
    if char in vowel:
        if char in counts:
            counts[char] += 1
        else: counts[char] = 1
print("\nVowels are founded in the text: ")
for v,c in counts.items(): #.items() sẽ trả về cặp (key, value) cho từng phần tử.
    print(v,":",c)
print("\nSum of vowels is: ", sum(counts.values()))

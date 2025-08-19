# 52. Write a Python program to print all permutations with a given repetition number of characters
# of a given string
#Viết chương trình Python in ra tất cả các tổ hợp (permutations) với số ký tự cho trước, trong đó các ký tự có thể lặp lại.
import itertools

text = input("Nhập chuỗi: ")
n =int(input("Nhập số kí tự của mỗi hoán vị: "))
permutation = itertools.product(text, repeat=n)  #Nếu muốn có lặp lại ký tự thì ta dùng itertools.product. Nếu muốn không lặp lại ký tự thì ta dùng itertools.permutations.
print("Các hoán vị có lặp là: ")
for perm in permutation:
    print( "".join(perm) )
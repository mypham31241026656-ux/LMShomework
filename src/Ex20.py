# 20. Write a Python function to reverse a string if its length is a multiple of 4.
string = input("Enter a string: ")
if len(string) % 4 == 0:
    result = string[::-1]
    print("Result is: ",result)

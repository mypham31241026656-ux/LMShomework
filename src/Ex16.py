# 16. Write a Python function to insert a string in the middle of a string.
# Sample function and result :
# insert_sting_middle('[[]]<<>>', ' Python') -> [[Python]]
#insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
frame = input("Enter the frame: ")
string = input("Enter the string: ")
middle = len(frame) // 2
result = frame[:middle] + string + frame[middle:]
print(result)
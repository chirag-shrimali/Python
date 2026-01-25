# Problem Description: Print the first five letters of the English alphabet i.e. A, B, C, D and E.

'''
Example Output 
    A 
    B 
    C 
    D 
    E
'''

ch = input('Enter the Starting Characters : ')

# print(ch)
# print(chr(ord(ch) + 1))
# print(chr(ord(ch) + 2))
# print(chr(ord(ch) + 3))
# print(chr(ord(ch) + 4))

for i in range(1 , 6) :
    print(chr(ord(ch) + i - 1))
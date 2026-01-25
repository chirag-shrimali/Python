# Generally,String are the immutable means in the existing string which can be made by users then can't be change that string

# the declarations of String

# string = 'Chirag'
# print(string)
# print('---------------------')
# string = "Chirag"
# print(string)
# print('---------------------')
# string = """Chirag"""
# print(string)
# print('---------------------')
# string = '''Chirag'''
# print(string)
# print('---------------------')

# -----------------------------------------------------------------------------------------------------------------

# string = "Chirag"
# print(type(string)) # <class 'str'>

# string = 'Chirag'
"""
C --> 0 --> -6
h --> 1 --> -5
i --> 2 --> -4
r --> 3 --> -3
a --> 4 --> -2
g --> 5 --> -1
len(string) = 6
"""

# print(string[0]) # C
# print(string[4]) # a
# print(string[2]) # i
# # print(string[6]) # in the string index out of the range
# print(string[-3]) # r
# print(string[-5]) # h
# print(string[-7]) # in the string index out ofthe range

# string = 'Chirag'

# print(string) # Chirag

# for i in string :
#     print(i)
"""
Prints :-
C
h
i
r
a
g
"""

name = "Chirag123 "

print(name) # Chirag123

print("isalnum...",name.isalnum()) # True

print("isalpha...",name.isalpha()) # True

print("isdecimal...",name.isdecimal()) # False

print("isdigit...",name.isdigit()) # False

print("islower...",name.islower()) # False

print("isupper...",name.isupper()) # False

print("isnumeric...",name.isnumeric()) # False

print("isspace...",name.isspace()) # False

print("istitle...",name.istitle()) # True

# print(name) #   chirag shrimali  

# upp = name.upper()

# print(upp) #   CHIRAG SHRIMALI  

# low = name.lower()

# print(low) #   chirag shrimali  

# cap = name.capitalize()

# print(cap) #   chirag shrimali  

# tit = name.title()

# print(tit) #   Chirag Shrimali  

# lstr = name.lstrip()

# print(lstr) # chirag shrimali  

# rstr = name.rstrip()

# print(rstr) #   chirag shrimali

# st = name.strip()

# print(st) # chirag shrimali
"""
5. Write a Python program to reverse strings in a given list of string values using lambda.

Original lists:
['Red', 'Green', 'Blue', 'White', 'Black']
Reverse strings of the said given list:
['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
"""

list = ['Red', 'Green', 'Blue', 'White', 'Black']

list1 = []

# for i in list :
#     list1.append(i[ : : -1])

# print(list1)

x = tuple(map(lambda x : x[ : : -1] , list))

print(x)
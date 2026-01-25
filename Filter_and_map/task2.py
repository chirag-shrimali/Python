"""
6.
Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.

Orginal list:
[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
Numbers of the above list divisible by nineteen or thirteen:
[19, 65, 57, 39, 152, 190]
"""

list = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

# list1 = []

# for i in list :
#     if(i % 19 == 0 or i % 13 == 0) :
#          list1.append(i)

# print(list1)

x = tuple(filter(lambda x : x % 19 == 0 or x % 13 == 0 , list))

print(x)
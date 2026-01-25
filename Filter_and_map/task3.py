'''
7.
Write a Python program to find palindromes in a given list of strings using Lambda.

Orginal list of strings:
['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
List of palindromes:
['php', 'aaa']
'''

list = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']

# list1 = []

# for i in list :
#     if(i == i[ : : -1]) :
#         list1.append(i)

# print(list1)

x = tuple(filter(lambda x : x == x[ : : -1] , list))

print(x)
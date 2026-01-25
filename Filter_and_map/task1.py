'''
4. Write a Python program to remove all elements from a given list present in another list using lambda.

Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]
Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
'''

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]

list3 = []

# for i in list1 :
#     if i not in list2 :
#         list3.append(i)

# print(list3)

x = list(filter(lambda x : x not in list2 , list1))

print(x)
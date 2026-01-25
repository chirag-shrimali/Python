# list tasks :-

"""
l1 = [10 , 20 , 30 , 40 , 50 , 60 , 70 , 999 , 99 , 45 , 50]
"""

#     0    1    2    3    4    5    6     7    8    9    10

l1 = [10 , 20 , 30 , 40 , 50 , 60 , 70 , 999 , 99 , 45 , 50]

# l1.sort()
# print("\n",l1)

# task : 1 second largest element

# print("---------------------------------------------------------")

# print('Finding the second largest elements in the lists...\n')

# print(l1[-2])

# ------------------------------------------------------------------------------

# task : 2 second smallest element

# print("---------------------------------------------------------")

# print('Finding the second smallest elements in the lists...\n')

# print(l1[1])

# ------------------------------------------------------------------------------

"""
task : 3 
l1 = [121 , 134 , 567 , 890 , 141]
separate palindrome elements in to list  
output  : [121 , 141]
"""
# print("---------------------------------------------------------")

# l = [121 , 134 , 567 , 890 , 141]

# no = int(input("Enter the number that you want to take in the list : "))

# l = []

# for i in range(no) :
#     arg = int(input("Enter the elements : "))
#     l.append(arg)
# # print(l)

# l1 = []

# for i in l :
#     if str(i) == str(i)[ : : -1] :
#         l1.append(i)
# print(l1)

# -----------------------------------------------------------------

# l1 = int(input("Enter first list : "))
# l2 = int(input("Enter second list : "))
# l3 = int(input("Enter third list : "))
# l4 = int(input("Enter fourth list : "))
# l5 = int(input("Enter fifth list : "))

# l = [l1 , l2 , l3 , l4 , l5]

# print(l)

# ---------------------------------------------------------------

"""
Task - 4 :-
take list from user append all element in list and remove duplicate element in the list.
         input : [1 , 2 , 3 , 4 , 4 , 5 , 5 , 6 , 7 , 8 , 9 , 9 , 10]
         output : [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
"""

# no = int(input("Enter the number that you want to take in the list : "))

# l = []

# for i in range(no) :
#     arg = int(input("Enter the elements : "))
#     l.append(arg)
# print(l)

# l1 = []

# for i in l :
#     if i not in l1 :
#         l1.append(i)
# print(l1)

# -------------------------------------------------------------------------------------

'''
Write a Python program to find a list of integers with exactly two occurrences of nineteen
	 and at least three occurrences of five.  count 
	Return True otherwise False.
	Input:
	[19, 19, 15, 5, 3, 5, 5, 2]
	Output:
	True
	Input:
	[19, 15, 15, 5, 3, 3, 5, 2]
	Output:
	False
	Input:
	[19, 19, 5, 5, 5, 5, 5]
	Output:
	True
'''

# no = int(input("Enter the number that you want to take in the list : "))

# l = []

# for i in range(no) :
#     arg = int(input("Enter the elements : "))
#     l.append(arg)
# print(l)

# l1 = []

# for i in l1 :
#     if(l.count(19) == 2 and (l.count(5) >= 3)) :
#         print('True')
# else :
#     print("False")

# ---------------------------------------------------------------

# task  :1  sort the  below  list to  second element.

"""
l1 = [[1,3], [0,2], [5,-9]]
ouptut  : [[5,-9],[0,2],[1,3]]
"""

# bubble  sort :

# #      0      1      2
# l = [[1,3], [0,2], [5,-9]]

# no = len(l) # 3

# for i in range(no) :
#     for j in range(0 , no - i - 1) :
#         if(l[j][1] > l[j + 1][1]) :
#             l[j] , l[j + 1] = l[j + 1] , l[j]
# print(l)

# ----------------------------------------------------

# task :2  swap first and last element. 

"""
input  : l1=[1,2,3,4,5,6,7,8]
output : l1 =[8,2,3,4,5,6,7,1]
"""

# l1 = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8]

# for i in l1 :
#     temp = l1[0] 
# l1[0] = l1[-1]
# l1[-1] = temp
# print(l1)

# ------------------------------------------------------

# Tuple
# task 1 :  add in tuple last position.

"""
input  : t1=(12,2,3,4,5,67.89,99,77,44,22,11,67.89,2)
output  : t1=(12,2,3,4,5,67.89,99,77,44,22,11,67.89,2,"krishiv")
"""

# t1 = (12 , 2 , 3 , 4 , 5 , 67.89 , 99 , 77 , 44 , 22 , 11 , 67.89 , 2)

# t2 = "Chirag",

# print(t1)

# print('---------------------------------------------------------------')

# print(t1 + t2)

# --------------------------------------------------------------------------

# task : 2 

"""
input  : t1 =[(1,2,3),(4,5,6),(7,8,9)]
output : t1 =[(1,2,100),(4,5,100),(7,8,100)]   
"""

t1 = [(1,2,3) , (4,5,6) , (7,8,9)]

t2 = list(t1[0])

t3 = t2.pop()

t4 = t2.append(100)


a2 = list(t1[1])

a3 = a2.pop()

a4 = a2.append(100)


d2 = list(t1[2])

d3 = d2.pop()

d4 = d2.append(100)

l = tuple(t2),tuple(a2),tuple(d2)

print(t1)
print(list(l))

# print(tuple(t2),',',tuple(a2),',',tuple(d2))
# print(tuple(t2))
# print(tuple(d2))
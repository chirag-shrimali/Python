"""  
Write a Python code which will return the sum of the numbers of the list. 
Return 0 for an empty list. 
Except the number 13 is very unlucky, so it does not count and number that come immediately after 13 also do not count 
in sum. 

Example : 
[1, 2, 3, 4] = 10 
[] = 0
[1, 2, 3, 4, 13] = 10 
[13, 1, 2, 3, 13] = 5
[1, 13, 2, 3, 4] = 8
"""

# l1 = int(input("\nEnter the No1 : "))
# l2 = int(input("\nEnter the No2 : "))
# l3 = int(input("\nEnter the No3 : "))
# l4 = int(input("\nEnter the No4 : "))

sum = 0

list = [1, 13, 2, 3, 4]

# for i in list :
#     if(list.count(i) == 0) :
#         sum = 0
#     elif list.index(13) or list.index(13) + 1 :
#         sum = sum + i
#     else :
#         sum = sum + i # sum += i

# print(sum)

i = 0

while i < len(list) :
    if(list[i] == 13) :
        i = i + 2
    else :
        sum = sum + list[i]
        i = i + 1 # i++ # i += 1
print(sum)
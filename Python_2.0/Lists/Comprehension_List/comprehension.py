# in the python , the list having the it's comprehension version

# upper all the elements in the lists ---------------------------------------------------------------------------------

# users = ["Chirag" , "Ramesh" , "Suresh" , "Mahesh" , "Mukesh" , "Ganesh"]

# # users1 = []

# # for i in users :
# #     users1.append(i.upper())

# # print(users1)

# # Comprehension Version...

# users2 = []

# users2 = [i.upper() for i in users]

# print(users2)

# display only first characters in the lists ----------------------------------------------------------------------------------------

# users = ["Chirag" , "Ramesh" , "Suresh" , "Mahesh" , "Mukesh" , "Ganesh"]

# # users1 = []

# # for i in users :
# #     users1.append(i[0])

# # print(users1)

# # Comprehension Version...

# users2 = []

# users2 = [i[0] for i in users]

# print(users2) 

# Adding 10 numbers in the given lists -----------------------------------------------------------------

# no = [100 , 200 , 300 , 400]

# # no1 = []

# # for i in no :
# #     no1.append(i + 10)

# # print(no1)

# # Comprehension Version

# no2 = []

# no2 = [i + 10 for i in no]

# print(no2)

# 10% Profit --------------------------------------------------------------------

no = [100 , 200 , 300 , 400]

# no1 = []

# for i in no :
#     no1.append(i * 1.1)

# print(no1)

# Comprehension Version...

no2 = []

no2 = [i * 1.1 for i in no]

print(no2)
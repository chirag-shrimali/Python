# write the python program and also write the comprehension version using if condition statements

# displays the lists which have length more than 4 ----------------------------------

# users = ["ram" , "shyam" , "amit" , "sumit" , "geeta" , "jaya" , "rama"]

# users1 = []

# for i in users :
#     if len(i) > 4 :
#         users1.append(i)

# print(users1)

# Comprehension Version ----------------

# users2 = [i for i in users if len(i) > 4]

# print(users2)

# -------------------------------------------------------------------------------------------------------

# Palindrome print 'yes' otherwise print 'no' ------------------------

# users = ["ram" , "shyam" , "amit" , "sumit" , "naman" , "geeta" , "madam" , "jaya" , "rama" , "bob"]

# users1 = []

# for i in users :
#     if(i == i[ : : -1]) :
#         users1.append(i)

# print(users1)

# users = ["ram" , "shyam" , "amit" , "sumit" , "naman" , "geeta" , "madam" , "jaya" , "rama" , "bob"]

# users1 = []

# for i in users :
#     if(i == i[ : : -1]) :
#         users1.append("Yes")
#     else :
#         users1.append("No")

# print(users)

# print(users1)

# Comprehension Version -------------------------------------------------

# users = ["ram" , "shyam" , "amit" , "sumit" , "naman" , "geeta" , "madam" , "jaya" , "rama" , "bob"]

# users1 = ["Yes" if i == i[ : : -1] else "No" for i in users]

# print(users)

# print(users1)

# --------------------------------------------------------------------------------------------------

# given numbers print zero if no is 0 pos when positive numbers and print neg when numbers is negative

# numbers = [-100 , 100 , 0 , 20 , 0 , -90 , 98 , 97 , 67 , -32]

# numbers1= []

# for i in numbers :
#     if(i > 0) :
#         numbers1.append("Pos")

#     elif i < 0 :
#         numbers1.append("Neg")

#     else :
#         numbers1.append("Zero")

# print(numbers)

# print(numbers1)

# Comprehension Version ----------------------------------

# numbers = [-100 , 100 , 0 , 20 , 0 , -90 , 98 , 97 , 67 , -32]

# numbers1 = ["Pos" if i > 0 else("Neg" if i < 0 else "Zero") for i in numbers]

# print(numbers)

# print(numbers1)

# ---------------------------------------------------------------------------------------------------------

# in the existing lists check the elements in the sales that which are greater than 50 and also print even for even numbers and odd for the odd numbers

# sales = [100 , 20 , 45 , 67 , 89 , 120 , 89 , 78]

# sales1 = []

# sales2 = []

# for i in sales :
#     if i > 50 and i % 2 == 0 :
#         sales1.append("Even")
#         sales2.append(i)
#     if i > 50 and i % 2 != 0 :
#         sales1.append("Odd")

#         sales2.append(i)

# print(sales2)

# print(sales1)

# Comprehension Version ------------------------

sales = [100 , 20 , 45 , 67 , 89 , 120 , 89 , 78]

sales1 = ["Even" if i % 2 == 0 else "Odd" for i in sales if i > 50]

print(sales1)
# Enumrate ------------------------

users = ["Chirag" , "Shyam" , "Ram" , "Suresh" , "Rahul"]

# for i in range(0 , len(users)) :
    
#     print(i , users[i])

# -----------------------------------------------------------------------

# for i in range(0 , len(users)) :

#     print("i" , i , users[i])

# -----------------------------------------------------------------------

# for i in range(0 , len(users)) :

#     print(i)

# -----------------------------------------------------------------------

# for index , elements in enumerate(users) :

#     print(f"INDEX : {index} VALUE : {elements}")

# -----------------------------------------------------------------------

# All and Any ------------------------

'''

all --> It will be return the boolean value data types but return True if all the conditions are true otherwise False...

any --> It will be return the boolean value data types but return True if any one conditions is satisfy otherwise False if any one conditions is not satisfying...

'''

# marks = [45 , 69 , 36 , 78 , 21]

# flag = True

# for i in marks :

#     if i > 50 :

#         flag = False

#         break

# print(marks)

# -----------------------------------------------------------------------

# marks = [14 , 69 , 36 , 78 , 21]

# flag = all(m > 30 for m in marks)

# print(flag)

# flag1 = any(m > 30 for m in marks)

# print(flag1)

# -----------------------------------------------------------------------

# Sorted ------------------------

# no = [4 , 6 , 3 , 8 , 5]

# print(no)

# no.sort()

# print(no)

# SORTED -----------------------------------------------------------------------

# no = [4 , 6 , 3 , 8 , 5]

# print(no)

# sort = sorted(no)

# print(sort)

# REVERSE -----------------------------------------------------------------------

# no = [4 , 6 , 3 , 8 , 5]

# print(no)

# sort = sorted(no , reverse = True)

# print(sort)

# STRING SORTED , REVERSE -----------------------------------------------------------------------

# users = ["Chirag" , "Suresh" , "Mahesh" , "Ganesh"]

# print(users)

# sortUsers = sorted(users)

# print(sortUsers)

# sortReverseUsers = sorted(users , reverse = True)

# print(sortReverseUsers)

# SORTED & REVERSE BY LENGTH -----------------------------------------------------------------------

# users = ["Chirag" , "Shyam" , "Ketan" , "Raj"]

# print(users)

# sortUsers = sorted(users , key = len)

# print(sortUsers)

# sortReverseUsers = sorted(users , key = len , reverse = True)

# print(sortReverseUsers)

# -----------------------------------------------------------------------

# no = [14 , 5 , -5 , 0 , 23 , -12]

# print(no)

# sort = sorted(no)

# print(sort)

# IGNORING BY SIGNED -----------------------------------------------------------------------

# no = [14 , 5 , -5 , 0 , 23 , -12]

# print(no)

# sort = sorted(no , key = lambda x : abs(x))

# print(sort)

# -----------------------------------------------------------------------

# x = 100

# print(x) # 100

# y = -100

# print(y) # -100

# z = abs(y)

# print(z) # 100

# TUPLE -----------------------------------------------------------------------

students = [("harsh" , 80) , ("raj" , 81) , ("parth" , 77)]

print(students)

sort = sorted(students) # sorting the tuples data by the string's first alphabets

print(sort)

sort1 = sorted(students , key = lambda x : x[1]) # Sorted by the marks

print(sort1)

sort2 = sorted(students , key = lambda x : x[1] , reverse = True) # Sorted by the marks reverse

print(sort2)
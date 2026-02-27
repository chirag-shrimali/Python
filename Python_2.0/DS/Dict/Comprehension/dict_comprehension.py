# in the data structure , the dictionary has comprehension version...

# {1 : 1 , 2 : 2 , 3 : 3 , 4 : 4 , 5 : 5}

# data = {}

# for i in range(1 , 6) :
#     data[i] = i # data[1] = 1

# print(data)

# # Comprehension Version...

# data1 = {i : i for i in range(1 , 6)}

# print(data1)

# -------------------------------------------------------------

# {1 : 1 , 2 : 4 , 3 : 9 , 4 : 16 , 5 : 25}

# data = {}

# for i in range(1 , 6) :
#     #  data[i] = i * i
#     data[i] = i ** 2

# print(data)

# # data1 = {i : i * i for i in range(1 , 6)}

# data1 = {i : i ** 2 for i in range(1 , 6)}

# print(data1)

# ----------------------------------------------------------

# data = ["amit" , "sumit" , "raj" , "parth" , "jay" , "kunal" , "sneha"]

# dic = {}

# # for i in data :
# #      dic[i] = i

# # print(dic)

# for i in data :
#      dic[i] = len(i)

# print(dic)

# # dic1 = {i : len(i) for i in data}

# # print(dic1)

# # dic1 = {i[0] : i for i in data}

# # print(dic1)

# dic1 = {i : len(i) for i in data if len(i) > 4}

# print(dic1)

# # {naman : "palindrome" , "ram" : "not"}

# -----------------------------------------------------------------

# names = ["naman" , "ram" , "shyam" , "bob" , "jay" , "madam"]

# # data = {i : i for i in names}

# data = {i : "palindrome" if i == i[ : : -1] else "Not Palindrome"  for i in names}

# print(data)

# Task - 1 ----------------------------------------------------------

# numbers = [25 , ....] # even odd 

# data = [25 , 30 , 69 , 78 , 45 , 36 , 37]

# dic = {i : "Even" if i % 2 == 0 else "Odd" for i in data}

# print(dic)

# Task - 2 ----------------------------------------------------------

# marks = {"Samir" : 85 , "Rahul" : 40 , "Aman" : 72}

# result = {'Samir' : 'Pass' , 'Rahul' : 'Fail' , 'Aman' : 'Pass'}

# dic1 = {i : "Pass" if marks[i] > 40 else "Fail" for i in marks}

# print(dic1)

# Task - 3 -----------------------------------------------------------

# data = {"a" : 1 , "b" : 2 , "c" : 3}

# data ={1 : "a" , 2 : "b" , 3 : "c"}
 
# # dic = {i : data[i] for i in data}

# dic = {i : data[i] for i in data}

# dic1 = {data[i] : i for i in data}

# # a , a + 1 = a + 1 , a

# print(dic)

# print(dic1)

# Task - 4 ------------------------------------------------------------

# data = {"name" : "samir", "city" : "ahmedabad"}

# # {'NAME' : 'samir' , 'CITY' : 'ahmedabad'}

# dict = {i.upper() : data[i] for i in data}

# print(dict)

# Task - 5 --------------------------------------------------------------

# Remove Negative Values

data = {"a" : 10 , "b" : -5 , "c" : 20 , "d" : -2}

dic = {i : data[i] for i in data if data[i] > 0}

print(dic)
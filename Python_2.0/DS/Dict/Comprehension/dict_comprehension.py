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

data = ["amit" , "sumit" , "raj" , "parth" , "jay" , "kunal" , "sneha"]

dic = {}

# for i in data :
#      dic[i] = i

# print(dic)

for i in data :
     dic[i] = len(i)

print(dic)

# dic1 = {i : len(i) for i in data}

# print(dic1)

# dic1 = {i[0] : i for i in data}

# print(dic1)

dic1 = {i : len(i) for i in data if len(i) > 4}

print(dic1)
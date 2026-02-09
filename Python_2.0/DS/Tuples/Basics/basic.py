# in the python the parts of data structures has data types like tuples

# the declarations of Tuples are : ()

# Empty Tuple ---------------------------------------------

# t = ()

# print(t) # () as Empty Tuples

# print(type(t)) # <class 'tuple'>

# print(type(t).__name__) # tuple as string

# Single Tuple Elements ------------------------------------

# t = (1 ,)

# print(t) # (1 ,)

# print(type(t)) # <class 'tuple'>

# print(type(t).__name__) # tuple as string

# t = (1) # or we can be write as t = 1

# print(t) # 1

# print(type(t)) # <class 'int'>

# print(type(t).__name__) # int

# Multiple Elements in the tuples ---------------------------------------------------

#    0   1      2          3               4          5

# t = (4 , 5 , "Chirag" , "Ahmedabad" , "Chirag@1234" , 99)

# print(t) # print all the elements which are present in the tuples

# print(type(t)) # <class 'tuple'>

# print(type(t).__name__) # tuple as string prints

# we can not assign any elements values of their indexing likes

# t[2] = "chirag"

# print(t[2]) # it will be shows error because in the tuples objects item assignments are not to be supported...

# t[1] = 9

# print(t[1]) # it will be also showing the same errors that tuple objects(elements) can't supported item assignment operators

# t = (4 , 5 , 9 , 7)

# # <class 'tuple'>   
# print(type(t) == tuple) # True

# # return as string tuple
# print(type(t).__name__ == "tuple") # True

#    0       1      2   3        4        5
t = (5 , "Chirag" , 9 , 7 , 'Ahmedabad' , 4)

# for i in t :
#     print(i)

for i in range(0 , len(t)) :
    print(i , '-' , t[i])
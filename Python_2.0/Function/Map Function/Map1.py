# '''

# Syntax of Map Function :-

# map(function like lambda or user defined function , iterable objects)

# '''

# users = ["Chirag" , "Rahul" , "Mahesh" , "Ganesh" , "Ramesh" , "Paresh"]

# print(users)

# users1 = map(lambda x : x , users)

# # print(users1) # it will be return the map object of users1

# print(list(users1))

# def data(*args) :
#     print(args)

# data([21 , "Chirag" , True , None , "Mukesh"])


# def getFullName(**kwargs):
    
#     def find():
#         for i in kwargs.values() :
#             ans = i.lower()
#             print(ans)
    
#     return find()

# x = getFullName(name="MahendraSingh",lname="Dhoni")
# #output mahedrasing-dhoni
# print(x)

data = [1 , 2 , 3]

s = str(data)

print('-'.join(s))
# Tuples have basically two built - in methods index and count

# Count ---------------------------------------------------------

#             0          1          2          3          4          5          6          7 

# users = ("Chirag" , 'Ramesh' , "Mukesh" , 'Ganesh' , "Paresh" , 'Ramesh' , "Suresh" , "Ramesh")

# print(users) # print all the elements of the users

# print(type(users)) # <class 'tuple'>

# print(type(users).__name__) # tuple as string print

# print(users.count("Ramesh")) # 3 it will be print the count of the Ramesh string that how many times in the tuples the elements name as Ramesh are there it will be prints the numbers of there if not present then it will be prints 0

# print(users.count("Mahesh")) # 0

# print(users.count("Chirag")) # 1

# print(users.count('chirag')) # 0

# Index --------------------------------------------------------

#             0          1          2          3          4          5          6          7 

users = ("Chirag" , 'Ramesh' , "Mukesh" , 'Ganesh' , "Paresh" , 'Ramesh' , "Suresh" , "Ramesh")

print(users) # prints all the elements of the users tuples

print(type(users)) # <class 'tuple'>

print(type(users).__name__) # tuple as string print

print(users.index("Mukesh")) # 2 it will be print the index value of the elements if they are present in the tuples otherwise it will be showing errors

print(users.index('Ramesh')) # 1 if the elements are reapeating multiple times the index() function will be print the first index value of that elements that where that elements are comes first times

print(users.index("chirag")) # error shows that tuple index which are not present in the existing tuples
# in the sets there are having so many operations of the sets like union , intersect , difference , symmetric difference , ... , etc.

data1 = {"Chirag" , "Suresh" , "Ramesh" , "Ganesh" , "Mukesh" , "Paresh"}

data2 = {"Suresh" , "Chirag" , "Ram" , "Shyam" , "Pratham" , "Rajesh" , "Ganesh"}

# print(data1) # it will be print the data - 1 values 

# print(data2) # it will be print the data - 2 values

# Union -----------------------------

# x = data1.union(data2)

# print(x) # {"Chirag" , "Suresh" , "Ramesh" , "Ganesh" , "Mukesh" , "Paresh" , "Ram" , "Shyam" , "Pratham" , "Rajesh"}

# x = data1 | data2

# print(x) # {"Chirag" , "Suresh" , "Ramesh" , "Ganesh" , "Mukesh" , "Paresh" , "Ram" , "Shyam" , "Pratham" , "Rajesh"}

# Intersection --------------------------

# x = data1.intersection(data2) # common elements(members) are printing

# print(x) # {"Suresh" , "Chirag" , "Ganesh"}

# x = data1 & data2

# print(x) # {"Suresh" , "Chirag" , "Ganesh"}

# Difference -----------------------------

# x = data1.difference(data2)

# print(x) # {"Ramesh" , "Mukesh" , "Paresh"}

# x = data1 - data2

# print(x) # {"Ramesh" , "Mukesh" , "Paresh"}

# Symmetric Difference ----------------------

# x = data1.symmetric_difference(data2)

# print(x) # {"Ramesh" , "Mukesh" , "Paresh" , "Ram" , "Shyam" , "Pratham" , "Rajesh"}

# IsSuper Set --------------------------------

# item1 = {1 , 5 , 6 , 2}

# item2 = {2 , 6 , 5}

# x = item1.issuperset(item2) # Item1 is a superset of Item2

# print(x)

# IsSub Set -----------------------------------

item1 = {5 , 2}

item2 = {2 , 6 , 5 , 1}

x = item1.issubset(item2) # item1 subset item2

print(x)
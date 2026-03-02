# in the python , the data structure of the sets which will be adding or updating the elements with unorder way with iterable all data structure like lists , string , tuples , ...

# Add(Only One Argument which will be add if present in the sets it will be remove duplicate automatically) -------------------------------

# data = {"Chirag" , "Ramesh" , "Suresh"}

# print(data)

# data.add("Rahul") # the add function takes only one arguments and will be add the elements in unorder way...

# print(data)

# print(type(data)) # <class 'set'>

# Update(Multiple Argument which will be add if present in the sets it will be remove duplicate automatically) -----------------------------

data = {"Chirag" , "Ramesh" , "Suresh"}

print(data)

# data.update({"Rahul" , "Mahesh" , "Chirag"}) # Set Way

# data.update(["Rahul" , "Mahesh" , "Chirag"]) # List Way

# data.update(("Rahul" , "Mahesh" , "Chirag")) # Tupple Way

data.update("Chirag") # if the updating elements are present in the sets then it will be remove them automatically and give us unordered way but with out duplication sets...

print(data)

print(type(data)) # <class 'set'>
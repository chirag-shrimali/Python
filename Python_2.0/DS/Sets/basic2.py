# in the python , there are having the methods of build - in like pop() which can be remove the elements unorder way...

# Pop ------------------------------

# data = {"Chirag" , "Ramesh" , "Mahesh"}

# print(data) # it will be print the whole set elements with unordered way...

# removeEle = data.pop() # unordered way removing...

# print("The Removing Elements is :",removeEle)

# print(data)

# print(type(data)) # <class 'set'>

# Remove -----------------------------

# data = {"Chirag" , "Ramesh" , "Mahesh"}

# print(data) # it will be print the whole set elements with unordered way...

# data.remove("Ramesh") # it will be remove the particular elements which can be present in the sets if not present then it will be showing errors...

# # data.remove("Ramesha") # KeyError: 'Ramesha'

# print(data)

# print(type(data))

# Discard -----------------------------

data = {"Chirag" , "Ramesh" , "Mahesh"}

print(data) # it will be print the whole set elements with unordered way...

# data.discard('Mahesh') # it will be remove the elements if present otherwise it will be not showing error by default all the elements values can be displays...

# print(data)

data.discard('Mahesha') # if not present not showing error...

print(data)

print(type(data)) # <class 'dict'>
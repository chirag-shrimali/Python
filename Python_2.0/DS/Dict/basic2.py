# in the python if we can be want to get the data of the dictionary we can be use get or [] passing by the keys...

data = {1 : "Chirag" , 2 : "Ramesh" , 3 : "Mukesh"}

print(data)

# print(data.get(3)) # Mukesh it will be returning the value at that keys

# print(data.get(33)) # None if the key is not present the get function will be return as None

# print(data[2]) # Mukesh it will be also return the value at that keys

# print(data[25]) # if the entering value of the key is not present it will be return the error as KeyError

# pop which can be remove the value of key and key also --------------------------------------------

# data.pop(2)

# print(data)

# ---------------------------------------------------------------------------------------------

# if 1 in data :
    
#     removeEle = data.pop(1)
    
#     print("\nRemoving Elements Value is :",removeEle) # it will be print only value of the key which can be remove...

# else :
#     print("\nNot Available...")
    
# print(data)

# -------------------------------------------------------------------------------------------

# removeEle = data.popitem()

# print(removeEle) # it will be print the tuple of the dictionary which can be removed...

# print(data)

# -------------------------------------------------------------------------------------------

# if the key is found then it will not be see the default value so it will not be return any default value

# but if the key value is not found it will be return the default value with out showing errors

# removeEle = data.pop(2 , "a") # syntax :- pop(key , defaultvalues)

# removeEle = data.pop(104 , 1)

# removeEle = data.pop(104 , "Chirag")

# removeEle = data.pop(104 , "abc")

# removeEle = data.pop(104 , False)

# removeEle = data.pop(104 , None)

removeEle = data.pop(101 , 56.78)

print(removeEle)

print(data)
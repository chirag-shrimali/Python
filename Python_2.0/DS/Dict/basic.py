# in the python , the data structure of python has dictionary...

# a = {key : value}

data = {"Ahmedabad" : "Gujarat" , "Delhi" : "Rajasthan" , "Manipur" : "Rajkot"}

# print(data) # it will be print the whole dictionary data

# print(data.get("Delhi")) # it will be return None if the given key's value are not present in the dictionary

# print(data["Delhi"]) # if the key is present then return that key value if not present then it will be return error

# print(type(data)) # <class 'dict'>

# Keys -----------------------------------------------------------------------------------------

# k = data.keys()

# print(k) # it will be return the all the keys value of the dictionary

# Values ---------------------------------------------------------------------------------------

# v = data.values()

# print(v) # it will be return the all the values of the dictionary

# Items (Keys / Values both) -------------------------------------------------------------------

# item = data.items()

# print(item)

# for i in data :
#     print(i) # it will be print the keys data 

# item = data.items()

# for i , j in item :
#     print(f"{i} - {j}")

# Updated dictionary ---------------------------------------------------------------------------

print(data)

data["Ahmedabad"] = "Diu"

data["Jaipur"] = "Mahastra"

print(data)

data.update({"Chennai" : "Banglore" , "Kolkata" : "Ranchi" , "Ahmedabad" : "Isanpur"})

print(data)
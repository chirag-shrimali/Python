data = {"Virat" : [122 , 150 , 60] , "Rohit" : [45 , 140 , 188]}

# print(data)

# print(data.keys()) # it will be print the keys of the data here it will be prints like dict_keys(['Virat' , 'Rohit'])

# print(data.values()) # it will be print the values of keys here it will be print like dict_values([[122 , 150 , 60] , [45 , 140 , 188]])

# print(data.items()) # it will be print the whole dictionary items data here like will be print like dict_items([('Virat' , [122 , 150 , 60]) , ('Rohit' , [45 , 140 , 188])])

# print(data.get("Rohit")) # if the user enter the key which will be present then it will be return their values otherwise it will be print as None

# print(data.get("Rahul")) # None

# print(data['Virat'])

# print((data["Dhoni"])) # it will be throw an error exception as the KeyError

# ---------------------------------------------------------------------------------

# x = data["Rohit"][1]

# print(data.get('Virat')[1])

# x = data["Rohit"][0]

# x = data["Rohit"][2]

# x = data["Rohit"][3] # it will be show the error as list index out of the range throw error as IndexError

# Update ----------------------------------------------------------------------------------

# print(data)

# x = data["Rohit"][1] = 150

# print(data)

# print(x)

# update the another way -------------------------------------------------------------------

# print(data)

# g = data.get('Virat')

# g[1] = 200

# print(data)

# print(g)

# ------------------------------------------------------------------------------------------

# print(data)

# data.update({'Hardik' : [78 , 90]})

# print(data)

# ------------------------------------------------------------------------------------------

# Items Print -----

# for i , j in data.items() :
#     print(f"{i} - {j}")

# Keys Print -----

# for i , j in data.items() :
#     print(f"{i}")

# Values Print -----

for i , j in data.items() :
    print(f"{j}")

for i , j in data.items() :
    print("------------")
    for run in j :
        print(run)
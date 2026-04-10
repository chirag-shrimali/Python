'''

names = ["amit" , "neha" , "smruti" , "priya" , "ajna" , "amita" , "mayavati" , "sushila" , "radha" , "jay"]

'''

names = ["amit" , "neha" , "smruti" , "priya" , "ajna" , "amita" , "mayavati" , "sushila" , "radha" , "jay"]

print(names)

names1 = map(lambda x : x.upper() , filter(lambda x : x.endswith('a') , names))

# print(names1) # it will be return the filter object of names1

print(list(names1))
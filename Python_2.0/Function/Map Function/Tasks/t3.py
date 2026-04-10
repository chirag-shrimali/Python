"""

using map and filter in the names the i contains return in upper in other lists...

"""

names = ["amit" , "neha" , "smruti" , "priya" , "ajna" , "amita" , "mayavati" , "sushila" , "radha" , "jay"]

print(names)

names1 = map(lambda x : x.upper() , filter(lambda x : 'i' in x , names))

print(list(names1))
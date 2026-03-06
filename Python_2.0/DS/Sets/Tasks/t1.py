mumbai ={"raj" , "parth" , "amit" , "sumit"}

pune = {"jay" , "amit" , "kunal" , "neha"}

goa = {"rajvi" , "priya" , "amit" , "neha" , "krishna" , "raj"}

# Task - 1 : find user who have attended all 3 events

# x = mumbai.intersection(pune).intersection(goa)

# print(x)

# Task - 2 : find user who is present in mumbai and goa

# x = mumbai.union(goa)

# print(x)

# Task - 3 : find user who is present in pune and goa

# x = pune | goa

# print(x)

# Task - 4 : find user who is present in mumbai and goa but not in pune

# x = mumbai.union(goa).difference(pune)

# print(x)

# Task - 5 : find user who is not present goa but mumbai and pune both

x = mumbai | pune - goa

print(x)
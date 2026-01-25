# Slicing---------------------------------------------------------------

# ---------------------------------------------------------------

# name = "java"

# print(name) # java

# print(name[0]) # j

# print(name[1]) # a

# print(name[2]) # v

# print(name[3]) # a

# # print(name[4]) # string index out of the range

# ---------------------------------------------------------------

# print(name[-1]) # a

# print(name[-2]) # v

# print(name[-3]) # a

# print(name[-4]) # j

# print(name[-5]) # string index out of the range

# ---------------------------------------------------------------

# name = "Chirag"

# print(name) # Chirag

# # Chirag
# print(name[0:6]) # range starts with 0 and goes upto 5 because 6 can be excluded...

# print(name[0:len(name)]) # Chirag

# # Chirag
# print(name[0:]) # goes upto 0 to length...

# # Chirag
# print(name[:6]) # goes 0 to 6

# print(name[2:5]) # ira

# print(name[1:4]) # hir

# ---------------------------------------------------------------

name = "Chirag"

print(name[4::-1])
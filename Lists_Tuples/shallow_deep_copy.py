# Shallow Copy :-

# l1 = [1 , 2 , 3 , 4 , 5]

# l2 = []

# print(l1) # [1 , 2 , 3 , 4 , 5]

# l2 = l1

# print(l2) # [1 , 2 , 3 , 4 , 5]

# l2.append(6)

# print(l1) # [1 , 2 , 3 , 4 , 5 , 6]

# print(l2) # [1 , 2 , 3 , 4 , 5 , 6]

# Deep Copy :- 

l1 = [1 , 2 , 3 , 4 , 5]

l2 = []

print(l1) # [1 , 2 , 3 , 4 , 5]

l2 = l1.copy()

print(l2) # [1 , 2 , 3 , 4 , 5]

l2.append(6)

print(l1) # [1 , 2 , 3 , 4 , 5]

print(l2) # [1 , 2 , 3 , 4 , 5 , 6]
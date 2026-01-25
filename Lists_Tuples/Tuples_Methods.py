# There are having different types of methods in tuples like count , index , ...

#    0   1   2   3   4   5   6   7   8   9
t = (5 , 4 , 7 , 1 , 6 , 3 , 5 , 4 , 5 , 6)

# count

# cnt = t.count(5)

# print(cnt)

# -------------------------------------------------------------------------------

# index

# idx = t.index(3)

# print(idx)

# -------------------------------------------------------------------------------

# concatenation

# t1 = (1 , 2 , 4)
# t2 = (5 , 6 , 8)

# concate = t1 + t2
# print(concate)

# -------------------------------------------------------------------------------

# Multiplying a tuple as users wants

# t1 = (1 , 2 , 3)

# mul = t1 * 4

# print(mul)

# -------------------------------------------------------------------------------

# checking that a particular elements are existing in a tuple or not

# t1 = (1 , 5 , 6)

# print(6 in t1) # True Return
# print(5 in t1) # True Return
# print(7 in t1) # Return False

# -------------------------------------------------------------------------------

# length checking of tuples

# t1 = (1 , 2 , 3 , 5)

# print(len(t1))

# -------------------------------------------------------------------------------

# Min Max checking of tuples elements

# t1 = (11 , 5 , 8 , 3 , 4)

# print(min(t1)) # min value return
# print(max(t1)) # max value return

# -------------------------------------------------------------------------------

# slicing

#     0   1   2   3   4
# t1 = (5 , 6 , 4 , 1 , 2)

# print(t1[2:4])

# -------------------------------------------------------------------------------

# unpacking

t1 = (5 , 6 , 8 , 7)

a , b , c , d , e = (5 , 6 , 8 , 7 , 8)

print(a , b , c , d , e)
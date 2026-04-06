# With out argument and with out return type...

'''

x = lambda : print("Hello World!!")

x()

'''

# -----------------------------------------------------------------------

# with argument but with out return type...

"""

x = lambda a , b : print(a + b)

x(1 , 2)

"""

# -----------------------------------------------------------------------

# With argument and with return type...

"""
1.

x = lambda a , b : a + b

print(x(1 , 2))

"""

'''
2.

x = lambda a , b , c : (a + b + c) / 3

# print(x(1 , 2 , 3)) # Or

ans = x(1 , 2 , 3)

print(ans)

'''

# 3.

x = lambda fname , lname : fname + " " + lname

print(x("Chirag" , "Shrimali")) # Or

ans = x("Suresh" , "Patel")

print(ans)
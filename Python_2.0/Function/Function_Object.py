# No argument no return type...

'''

def data() :
    
    print("Hello World!!")

    print("Data Function is Called...")

data() # prints the contexts of data function...

'''

# ----------------------------------------------------------------------

"""

def data() :
    
    print("Hello World!!")

    print("Data Function is Called...")

    return 10

x = data

print("X :" , x) # it will be prints the address of data function which can be assign to the variables of x...

x() # it will be prints the contexts of data function...

"""

# ------------------------------------------------------------------------------

def data(a , b , c) :
    
    print("Hello World!!")

    print("Data Function is Called...")

    return a + b + c

x = data

print("X :", x)

ans = x(1 , 2 , 3)

print(ans)

# ---------------------

print("--------------------------")

# Otherwise...

print(x(1 , 2 , 3))
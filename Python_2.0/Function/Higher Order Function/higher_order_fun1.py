"""

def data(a) :

    print("Data Function is Called...")

    print(f"A : {a}")

data("Chirag")

"""

# --------------------------------------------------------------------------------------------

'''

def data(a) :

    print("Data Function is Called...")

    print(f"A : {a}")

data("Chirag") # String Value

data(21) # Integer Value

data(True) # Boolean Value

data((1 , 2 , "Ramesh")) # Tuple

data([5 , 21 , "Suresh"]) # List

'''

# --------------------------------------------------------------------------------------------

"""
1.

def data(a) :

    print("Data Function is Called...")

    print(f"A : {a}") # Prints the address of call function...

def call() :
    
    print("Call Function is Called...")

data(call)

"""

'''
2.

def data(a) :

    print("Data Function is Called...")

    print(f"A : {a}") # Prints the address of call function...

def call() :
    
    print("Call Function is Called...")

    return 10

data(call())

'''

def data(a) :

    print("Data Function is Called...")

    print(f"A : {a}") # Prints the address of call function...

    a() # also write call() it will be prints the contexts of call function...

def call() :
    
    print("Call Function is Called...")

data(call)
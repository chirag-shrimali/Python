'''
In the Python , there are having 4 types of functions...

1. No Argument and No Return Type
2. No Argument and With Return Type
3. With Argument and No Return Type
4. With Argument and With Return Type
'''

# 1. No Argument and No Return Type

"""
def greet() :
    print("Hello , Chirag!!")

greet()

"""

# ---------------------------------------------------------------------

# 2. No Argument and With Return Type

'''
def getSum() :
    a = 10

    b = 2

    c = a + b

    return c

print(f"The Sum is : {getSum()}")
'''

# ---------------------------------------------------------------------

# 3. With Argument and No Return Type

'''
def greet(name) :
    print(f"Hello , {name}")

greet("Chirag")
'''

# ---------------------------------------------------------------------

# 4. With Argument and With Return Type

# CREATE A SIMPLE CALCULATOR USING FUNCTION 

def add(a , b) :
    return a + b

def sub(x , y) :
    return x - y

def mul(p , q) :
    return p * q

def div(r , s) :
    return r / s

def mod(c , d) :
    return c % d

print(f'The Addition is : {add(15 , 3)}') # 18

print(f'The Subtraction is : {sub(15 , 3)}') # 12

print(f'The Multiplication is : {mul(15 , 3)}') # 45

print(f'The Division is : {div(15 , 3)}') # 5.0 always remeber that in python if any number is divisible by another number then at the result always shows decimal parts like '.'

print(f'The Modulus is : {mod(40 , 7)}') # 5
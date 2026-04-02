# def users(x) :
    
#     print(x)

# any data types arguments can be passing here...

# users("ram","shyam") # Error because users() takes only one arguments / parameters 

# users(5)

# --------------------------------------------------------------------------------------

# Args is not a kayword we can also use the another variables to like (*name)...

'''

Args having the data types of tuples...

'''

# def users(*args) :
    
#     print(args)

# Empty Tuple

# users() # when we use args means * then any variables then we can give unlimited arguments as input...

# -----------------------

# users('Chirag' , 'Rahul') # two arguments as input valid

# -----------------------

# users(56 , 89.78 , True , 'Chirag' , None) # Valid

# -----------------------

# users('Chirag' , 21 , ('Shrimali' , )) # Valid

# -----------------------

# users('Chirag' , 21 , ('Shrimali' , 45 , ('Suresh' , 25.78 , ('Ramesh' , True , ('Mahesh' , None))))) # Valid

# --------------------------------------------------------------------------------------

'''

def students(*names , x) :
    
    print(f"Names...{names}")
    
    print('X :',x)

students('Chirag' , 'Suresh' , 'Ramesh') # Error comes because args which can be takes unlimited values as the input so in the 2nd arguments can't gets the required arguments as input thus error can be comes while running...

'''

# --------------------------------------------------------------------------------------

"""

def students(x , *names) :
    
    print(f"Names...{names}")
    
    print('X :',x)

students('Chirag' , 'Suresh' , 'Ramesh') # by default the first arguments which can be takes here arguments x and then names as args variables use takes the rest of the arguments... 

"""

# --------------------------------------------------------------------------------------

def students(*names , x) :
    
    print(f"Names...{names}")
    
    print('X :',x)

# students(x = 'Chirag' , 'Suresh' , 'Ramesh') # Error

# students('Chirag' , x = 'Suresh' , x = 'Ramesh') # Error because arguments x repeated twice times...

students('Chirag' , 'Suresh' , x = 'Ramesh') # Valid
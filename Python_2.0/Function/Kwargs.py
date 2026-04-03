'''
The Data type of the args is tuples...

args defined as *args...

where the data type of kwargs is dictionary...

kwargs defined as **kwargs... 
'''

"""

def getData(**kwargs) :
    print(f"Kwargs : {kwargs}")

# getData("Chirag" , "Ramesh" , 45 , 36) # Error occurs

# Compulsary name parameter through we can passing here because kwargs having the data types of dictionary so key and values both required...

getData(name = "Chirag" , marks = 99 , salary = 15000) 

"""

# ---------------------------------------------------------------------------

'''

def getData(x , **kwargs) :
    
    print("X = " , x)

    print("Kwargs : ",kwargs)

# getData(1000 , name = "Chirag" , age = 19 , salary = 15000) # Valid

# getData(x = 1000 , name = "Chirag" , age = 19 , salary = 15000) # Valid

# getData(name = "Chirag" , age = 19 , salary = 15000 , 1000) # Error

getData(name = "Chirag" , age = 19 , salary = 15000 , x = 1000) # Valid

'''

# ---------------------------------------------------------------------------

# Combinations of args and kwargs

def data(*args , **kwargs) :
    
    print(f"ARGS : {args}") # data types of args tuples...

    print(f"KWARGS : {kwargs}") # data types of kwargs dictionary...

data(10 , 20 , 30 , name = "Chirag" , age = 19 , salary = 15000)
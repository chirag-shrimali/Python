"""

def greet() :
    print("Hello , Chirag!!")

greet() # Valid and it will be print Hello , Chirag!!... 

greet(5 , 6) # error comes because greet function does not having taking any parameters / arguments... 

"""

'''

def demo() :

    print("Demo Function Called...")
    
    print("No Return type No Argument")

demo() # With out any error it will be prints the contents inside the demo() function...

'''

def add(a,b) :

    print("Addition Function Called...")
    
    print(a + b)

# add() # error comes because no arguments or parameters passing in add() functions...

# add(1 , 2) # it will be printing the sum of two numbers here it will be prints 3 as here and also printing the inside add(a , b) function contents... 

# add('Chirag' , "Shrimali") # it will be prints the things which out any error because in the python there is no particularly data types can be passing so any data types but having both same we are passing here with out error prints...

# add(5 , 'Chirag') # here we pass any data types but different at the same times passing errors we are getting here int + str invalid passing data types... 

# add(True , 55) # here we not getting error here python by default takes True values as 1 and take sum of it...

# add(False , 55) # False consider 0 so 55 + 0 = 55

add(True , False) # True as 1 and False as 0 thus 1 + 0 = 1
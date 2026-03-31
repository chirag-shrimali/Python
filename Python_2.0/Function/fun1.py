"""
Functions are having four types :-

1. With Argument and With Return Type
2. With Argument and No Return Type
3. No Argument and With Return Type
4. No Argument and No Return Type
"""

def getUserData(name , age , salary) :
    print(f"Name is : {name}")
    print(f"Age is : {age}")
    print(f"Salary is : {salary}")

# if i am writing only this it will be displaying me typeError that it can be requires 3 parameters or arguments

# getUserData()

# ---------------------------------------------------------------------------

# Valid Data

'''

getUserData("Chirag" , 19 , 25000)

print('----------------------------------------------')

'''

# ---------------------------------------------------------------------------

# Valid but not efficient to use...

# it can be sequencelly accepts the arguments / parameters as pased in getUserData()

'''

getUserData(19 , 25000 , "Chirag")

print('----------------------------------------------')

'''

# ---------------------------------------------------------------------------

'''

getUserData(salary = 50000 , age = 19 , name = 'Chirag') # this is also a valid way of writing and users want according write the parameters and write the values also...

print('----------------------------------------------')

'''

# ---------------------------------------------------------------------------

'''

getUserData('Chirag' , age = 19 , salary = 150000) # Valid

print('----------------------------------------------')

'''

# ---------------------------------------------------------------------------

'''

getUserData(age = 19 , 'Chirag' , salary = 15000) # Not Valid

print('----------------------------------------------')

'''

# ---------------------------------------------------------------------------

'''

getUserData("Chirag" , age = 19 , 23000) # Not Valid

print('----------------------------------------------')

'''

# ---------------------------------------------------------------------------

'''

getUserData(name = "Chirag" , age = 19 , name = 15000) # Not Valid passing 3 arguments but same parameters name(keyword argument repeated: name)...

print('----------------------------------------------')

'''

# ---------------------------------------------------------------------------

getUserData('Chirag' , 19 , age = 20) # Invalid age already sequence wise taken in the arguments(getUserData() got multiple values for argument 'age')...

print('----------------------------------------------')
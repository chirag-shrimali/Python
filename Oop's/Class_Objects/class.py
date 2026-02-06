# Oop's --> Object Oriented Programming Langauge

"""  
Class --> Blueprint of Object

Object --> Instances Of Class

Visibility of Scope :-
1. Public
2. Protected
3. Private

1. Public :- We can be access any data and also we can use the object to access the data it will be use any where...

2. Private :- We can not be create object for private data members and can't be use outside the class but we can use the data members functions to access it inside the class...

3.Protected :- We can also not be create object for the protected data members but we can be use it in the derived(sub) class and it can be inherited in the inheritance...   
"""

# class Variable Name
#        |
class Student :
    name = "Chirag Shrimali" # Data Members
    age = 19
    email = "chiragshrimali2147@gmail.com"
    city = "Ahmedabad"

# Object Create
s = Student()

# Displays

print(f"\nThe Name of Student is : {s.name}")

print(f"\nThe Age of Student is : {s.age}")

print(f"\nThe Email of the Student is : {s.email}")

print(f"\nThe City of the Student is : {s.city}")
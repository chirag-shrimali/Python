"""  
Inheritance :-
1. Single Inheritance
2. Multiple Inheritance
3. Multilevel Inheritance
4. Hierarchy Inheritance
5. Hybrid Inheritance

Constructors :-
1. Default Constructors
2. Parameterized Constructors
3. Copy Constructors
4. Non - Parameterized Constructors
5. Overloading Constructors Methods

Visibility Scope :-
1. Private --> __name
2. Public
3. Protected --> _name
"""

# Default Constructors :-

# class Student :
#     def __init__(self):
#         print("\nMy Name is Chirag Shrimali...")
#         print("\nMy Age is 19...")
#         print("\nMy Hobbies are playing cricket , chess , ... , etc.")

# # Object Created
# #      |
# s = Student()

# Non - Parameterized (also we can be call as Default Constructors) :-

# class Employee :
#     def __init__(self):
#         self.__emp_name = "Chirag Shrimali"
#         self.__emp_email = "chiragshrimali0411@gmail.com"
#         self.__emp_age = 19
#         self.__emp_salary = 15000

#         print("\nThis is a Non - Parameterized Constructors...")

#     def show(self) :
#         print("\nEmployee's Name :",self.__emp_name)

#         print("\nEmployee's Email :",self.__emp_email)
        
#         print("\nEmployee's Age :",self.__emp_age)
        
#         print("\nEmployee's Salary :",self.__emp_salary)

# e = Employee()

# e.show()

# if the data members are private or protected then we can't create or make object of it it will be give error at that times that time we only use functions to access that data...

# print(e.emp_name)

# print(e.emp_email)

# print(e.emp_age)

# print(e.emp_salary)

# Parameterized Constructors :- (Argument we are passing in the members functions or behaviours)

# class Car :
#     def __init__(self , color , price , model):
#         self.color = color # public
#         self.__price = price # private
#         self.model = model # public

#         print("\nThis is a Parameterized Constructors...")

#     def show(self) :
#         print("\nCar Color are :",self.color)

#         print("\nCar's Price are :",self.__price)

#         print("\nCar's Model are :",self.model)

# c = Car("White" , 150000 , "BMW")

# c.show()

# print(c.color)

# print(c.price)

# print(c.model)

# Methods Overloading Constructors :-

# class Animal :
#     def __init__(self):
#         print("\nThis is a Default Constructors...")

#     def __init__(self):
#         print("\nThis is a Non - Parameterized Constructors...")
#         self.dog = "bhaw"
#         self.cat = "meow"

#     def __init__(self , sound , color) :
#         print("\nThis is a Parameterized Constructors...")
#         self.sound = sound
#         self.color = color

#     def show(self) :
#         print("\nAnimal Sound are :",self.sound)
#         print("\nAnimal Color are :",self.color)

# a = Animal("bla bla!!" , "brown")

# a.show()

# print(a.sound)

# print(a.color)

# Deep and Shallow Copy in Class , Objects and Constructors...

import copy

class Student :
    def __init__(self , id , name , age):
        self.id = id
        self.name = name
        self.age = age
        print("\nThis is a Parameterized Constructors...")

    def show(self) :
        print("\nStudent's ID is :",self.id)
        print("\nStudent's Name is :",self.name)
        print("\nStudent's Age is :",self.age)

s = Student(1 , "Chirag" , 19)

# print(s.id , s.name , s.age)

s.show()

# module   shallow
# imports  copy
#     |     |
s1 = copy.copy(s)

# module    deep
# imports   copy
#      |      |
s2 = copy.deepcopy(s)

# print(s1)

# print(s2)

print(s1.id)

print(s1.name)

print(s2.age)

print(s2.name)
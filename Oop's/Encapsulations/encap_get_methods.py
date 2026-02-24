# in the python , Encapsulations having the methods name as Get Methods

class Student :
    def __init__(self):
        self.__name = "Chirag"
        self.__age = 18

    def get_name(self) :
        return self.__name
    
    def get_age(self) :
        return self.__age
    
s = Student()

print("\nThe Student Name is :",s.get_name()) # it will be print the name of student

print("\nThe Student Age is :",s.get_age()) # it will be print the age of student

s.__name = "Rahul" # no modify or update can be happens in the private visibility of scope

s.__age = 20 # no modify or update can be happens in the private visibility of scope

print("\nThe Student Name is :",s.get_name()) # it will be print the name of student

print("\nThe Student Age is :",s.get_age()) # it will be print the age of student
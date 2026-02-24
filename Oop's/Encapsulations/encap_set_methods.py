# in the python , Encapsulations having the methods name as Set Methods only through set methods we can be update or modify the private scope...

class Student :
    # Non - Parameterized Constructors
    def __init__(self):
        self.__name = "Chirag"
        self.__age = 19

    def set_name(self , __name) :
        self.__name = __name

    def set_age(self , __age) :
        self.__age = __age

    def get_name(self) :
        return self.__name
    
    def get_age(self) :
        return self.__age
    
s = Student()

print("\n----- Before the use of set methods -----")

print("\nThe Student Name is :",s.get_name())

print("\nThe Student Age is :",s.get_age())

s.set_name("Rahul")

s.set_age(45)

print("\n----- After the use of set methods -----")

print("\nThe Updated Student Name is :",s.get_name())

print("\nThe Updated Student Age is :",s.get_age())
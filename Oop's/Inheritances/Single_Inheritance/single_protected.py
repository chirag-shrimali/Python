"""  
There are having 5 types of inheritances...

1. Single Inheritance
2. Multi - Level Inheritance
3. Hierarchical Inheritance
4. Multiple Inheritance
5. Hybrid Inheritance
"""

# Single Inheritance :-

"""
    A
    |
    B(A) object to be created...
"""

# Scope Visibility (Protected) NON Parameterized ------------------------------------------------------------

# class student :
#     def __init__(self):
#         self._name = "Chirag"
#         self._age = 19

# class teacher(student) :
#     def __init__(self):
#         student.__init__(self)
#         self._t_name = "Kishor Kumar"

#     def show(self) :
#         print("\n======= Student Information =======")
#         print("\nStudent Name is :",self._name)
#         print("\nStudent Age is :",self._age)
#         print("\n======= Teacher Information =======")
#         print("\nTeacher Name is :",self._t_name)

# t = teacher()

# t.show()

# ----------------------------------------------------------------------------------

# class student :
#     def __init__(self):
#         self._name = "Mukesh"
#         self._age = 19

# class teacher(student) :
#     def __init__(self):
#         super().__init__()
#         self._t_name = "Ramesh Shah"

#     def show(self) :
#         print("\n======= Student Information =======")
#         print("\nStudent Name is :",self._name)
#         print("\nStudent Age is :",self._age)
#         print("\n======= Teacher Information =======")
#         print("\nTeacher Name is :",self._t_name)

# t = teacher()

# t.show()

# ------------------------------------------------------------------------------------------------

# class student :
#     # def __init__(self):
#         _name = "Chirag"
#         _age = 30   

# class teacher(student) :
#     def __init__(self):
#         self._t_name = "Ramesh Patel"

#     def show(self) :
#         print("\n======= Student Information =======")
#         print("\nStudent Name is :",self._name)
#         print("\nStudent Age is :",self._age)  
#         print("\n======= Teacher Information =======")
#         print("\nTeacher Name is :",self._t_name)

# t = teacher()

# t.show()

# Update or Modify ---------------------------------------------------------------------------------------------------

# class student :
#     def __init__(self):
#         self._name = "Chirag"
#         self._age = 19
    
# class teacher(student) :
#     def __init__(self):
#         student.__init__(self)
#         self._t_name = "Ramesh Shah"

#     def show(self) :
#         print("\n======= Student Information =======")
#         print("\nStudent Name is :",self._name)
#         print("\nStudent Age is :",self._age)
#         print("\n======= Teacher Information =======")
#         print("\nTeacher Name is :",self._t_name)

# t = teacher()

# t.show()

# print("\n------------------------------------------------------------------")

# t._name = "Chintan"

# t._t_name = "Bhvesh Prajapti"

# t._age = 45

# t.show()

# Parameterized Constrcutors -----------------------------------------------------------------

class student :
    def __init__(self , name , age , city):
        self._name = name
        self._age = age
        self._city = city

class teacher(student) :
    def __init__(self , name , age , city):
        student.__init__(self , name , age , city)
        self._t_name = "Kishor Kumar"

    def show(self) :
        print("\n======= Student Information =======")
        print("\nStudent Name is :",self._name)
        print("\nStudent Age is :",self._age)
        print("\nStudent City is :",self._city)
        print("\n======= Teacher Information =======")
        print("\nTeacher Name is :",self._t_name)

t = teacher("Chirag" , 19 , "Srinagar")

t.show()
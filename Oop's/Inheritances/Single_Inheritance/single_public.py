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

# Scope Visibility (Public) ------------------------------------------------------------

# class student :
#     def __init__(self):
#         self.name = "Chirag"
#         self.age = 19

# class teacher(student) :
#     def __init__(self):
#         student.__init__(self)
#         self.t_name = "Ramesh Shah"

#     def show(self) :
#         print("\n======= Student Information =======")
#         print("\nStudent Name is :",self.name)
#         print("\nStudent Age is :",self.age)
#         print("\n======= Teacher Information =======")
#         print("\nTeacher Name is :",self.t_name)

# t = teacher()

# t.show()

# ----------------------------------------------------------------------------------

# class student :
#     def __init__(self):
#         self.name = "Chirag"
#         self.age = 19

# class teacher(student) :
#     def __init__(self):
#         super().__init__()
#         self.t_name = "Ramesh Shah"

#     def show(self) :
#         print("\n======= Student Information =======")
#         print("\nStudent Name is :",self.name)
#         print("\nStudent Age is :",self.age)
#         print("\n======= Teacher Information =======")
#         print("\nTeacher Name is :",self.t_name)

# t = teacher()

# t.show()

# ------------------------------------------------------------------------------------------------

# class student :
#     # def __init__(self):
#         name = "Chirag"
#         age = 19

# class teacher(student) :
#     def __init__(self):
#         self.t_name = "Ramesh Shah"

#     def show(self) :
#         print("\n======= Student Information =======")
#         print("\nStudent Name is :",self.name)
#         print("\nStudent Age is :",self.age)
#         print("\n======= Teacher Information =======")
#         print("\nTeacher Name is :",self.t_name)

# t = teacher()

# t.show()

# Update or Modify ---------------------------------------------------------------------------------------------------

# class student :
#     def __init__(self):
#         self.name = "Chirag"
#         self.age = 19

# class teacher(student) :
#     def __init__(self):
#         student.__init__(self)
#         self.t_name = "Ramesh Shah"

#     def show(self) :
#         print("\n======= Student Information =======")
#         print("\nStudent Name is :",self.name)
#         print("\nStudent Age is :",self.age)
#         print("\n======= Teacher Information =======")
#         print("\nTeacher Name is :",self.t_name)

# t = teacher()

# t.show()

# print("\n------------------------------------------------------------------")

# t.name = "Chintan"

# t.age = 45

# t.show()

# Parameterized Constrcutors -----------------------------------------------------------------

class student :
    def __init__(self , name , age , city):
        self.name = name
        self.age = age
        self.city = city

class teacher(student) :
    def __init__(self , name , age , city):
        student.__init__(self , name , age , city)
        self.t_name = "Kishor Kumar"

    def show(self) :
        print("\n======= Student Information =======")
        print("\nStudent Name is :",self.name)
        print("\nStudent Age is :",self.age)
        print("\nStudent City is :",self.city)
        print("\n======= Teacher Information =======")
        print("\nTeacher Name is :",self.t_name)

t = teacher("Chirag" , 19 , "Srinagar")

t.show()
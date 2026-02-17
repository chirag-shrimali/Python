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

# Scope Visibility (Private) ------------------------------------------------------------

# class student :
#     def __init__(self):
#         self.__name = "Chirag"
#         self.__age = 19

#     def display(self) :
#         print("\nStudent Name is :",self.__name)
#         print("\nStudent Age is :",self.__age)

# class teacher(student) :
#     def __init__(self):
#         student.__init__(self)
#         self.__t_name = "Kishor Kumar"

#     def show(self) :
#         print("\n======= Student Information =======")
#         self.display()
#         print("\n======= Teacher Information =======")
#         print("\nTeacher Name is :",self.__t_name)

# t = teacher()

# t.show()

# ----------------------------------------------------------------------------------

# class student :
#     def __init__(self):
#         self.__name = "Mukesh"
#         self.__age = 19

#     def display(self) :
#         print("\nStudent Name is :",self.__name)
#         print("\nStudent Age is :",self.__age)

# class teacher(student) :
#     def __init__(self):
#         super().__init__()
#         self.__t_name = "Ramesh Shah"

#     def show(self) :
#         print("\n======= Student Information =======")
#         self.display()
#         print("\n======= Teacher Information =======")
#         print("\nTeacher Name is :",self.__t_name)

# t = teacher()

# t.show()

# ------------------------------------------------------------------------------------------------

# class student :
#     # def __init__(self):
#         __name = "Chirag"
#         __age = 30

#         def view(self) :
#             print("\nStudent Name is :",self.__name)
#             print("\nStudent Age is :",self.__age)     

# class teacher(student) :
#     def __init__(self):
#         self.__t_name = "Ramesh Patel"

#     def show(self) :
#         print("\n======= Student Information =======")
#         self.view()
#         print("\n======= Teacher Information =======")
#         print("\nTeacher Name is :",self.__t_name)

# t = teacher()

# t.show()

# Update or Modify ---------------------------------------------------------------------------------------------------

class student :
    def __init__(self):
        self.__name = "Chirag"
        self.__age = 19

    def display(self) :
        print("\nStudent Name is :",self.__name)
        print("\nStudent Age is :",self.__age)

class teacher(student) :
    def __init__(self):
        student.__init__(self)
        self.__t_name = "Ramesh Shah"

    def show(self) :
        print("\n======= Student Information =======")
        self.display()
        print("\n======= Teacher Information =======")
        print("\nTeacher Name is :",self.__t_name)

t = teacher()

t.show()

print("\n------------------------------------------------------------------")

t.__name = "Chintan"

t.__t_name = "Bhvesh Prajapti"

t.__age = 45

t.show()
'''
    A(Parent Class)
    |
    B(Child Class)
    |
    C

        C class can be inherited... 
'''

class User :

    def __init__(self , name) :
        
        print("User Class is Called!!")

        # Parameterized Constructors...

        self.name = name

class Employee(User) :

    def __init__(self, name) :
        
        super().__init__(name)

        print("Employee Class is Called!!")

    def showEmpDetails(self) :

        print(f"Employee Name is : {self.name}")

class Manager(User) : 

    def __init__(self, name) :
        
        super().__init__(name)

        print("Manager Class is Called!!")
    
    def showManDetails(self) :

        print(f"Manager Name is : {self.name}")

e = Employee("Chirag Shrimali")

e.showEmpDetails()

print("\n---------------------------------------------------------\n")

m = Manager("Ruturaj Gaikwad")

m.showManDetails()
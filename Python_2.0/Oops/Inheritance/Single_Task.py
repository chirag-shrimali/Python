class User :

    def __init__(self , name) :
        
        print("User Class is Called!!")

        self.name = name

class Employee(User) :

    def __init__(self, name) :
        
        print("Employee Class is Called!!")

        super().__init__(name)

    def getEmpInfo(self) :

        print("Employee Name :" , self.name)

class Manager(User) :

    def __init__(self, name) :

        print("Manager Class is Called!!")

        super().__init__(name)

    def getManInfo(self) :

        print("Manager Name :" , self.name)

e = Employee("Raju Patel")

e.getEmpInfo()

print("\n---------------------------------------------------------------\n")

m = Manager("Rajesh Patel")

m.getManInfo()
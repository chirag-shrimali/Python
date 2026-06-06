class User :

    def __init__(self , name) :
        
        print("User Class is Called!!")

        self.name = name

class Employee(User) :

    def __init__(self, name) :
        
        print("Employee Class is Called!!")

        super().__init__(name)

    def getEmpInfo(self) :

        fileE = open("Employee.txt" , "w")

        fileE.write(f"Employee Name : {self.name}")

        fileE.close()

class Manager(User) :

    def __init__(self, name) :

        print("Manager Class is Called!!")

        super().__init__(name)

    def getManInfo(self) :

        fileM = open("Manager.txt" , "w")

        fileM.write(f"Manager Name : {self.name}")

        fileM.close()

e = Employee("Raju Patel")

e.getEmpInfo()

print("\n---------------------------------------------------------------\n")

m = Manager("Rajesh Patel")

m.getManInfo()
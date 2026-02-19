# Hierarchical Inheritance :-

"""  
    A
  -----
 |     |
 B(A)  C(A)
"""

class Vehicle :
    def __init__(self):
        
        self.name = "Honda"
        
        self.average = 45.78

    def show(self) :
        
        print("\n---------- Vehicle Details ----------")
        
        print("\nThe Vehicle Name is :",self.name)

        print("\nThe Vehicle Average is :",self.average)

class Car(Vehicle) :
    def __init__(self , model):
        
        super().__init__()
        
        self.model = model

    def display(self) :
        
        self.show()

        print("\n---------- Car Details ----------")
        
        print("\nThe Car Model is :",self.model)

class Bike(Vehicle) :

    def __init__(self , speed):
        
        Vehicle.__init__(self) 

        self.speed = speed

    def view(self) :

        print("\n---------- Bike Details ----------")

        print("\nThe Bike Speed is :",self.speed)

c = Car("Tata")

c.display()

b = Bike(1500)

b.view()
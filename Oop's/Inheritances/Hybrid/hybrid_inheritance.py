# Hybrid Inheritance :-

"""  
    A
 -------
 |     |
 B(A)  C(A)
 -------
    |
    D(B , C)
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
    def __init__(self , model , **kwargs):
        
        super().__init__(**kwargs)
        
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

        self.display()

        print("\n---------- Bike Details ----------")

        print("\nThe Bike Speed is :",self.speed)

class Truck(Car , Bike) :
    
    def __init__(self, capacity , model , speed):
        
        super().__init__(model = model , speed = speed)

        self.capacity = capacity

    def see(self) :

        self.view()

        print("\nThe Truck Capacity is :",self.capacity)

t = Truck(1000 , "Tyoto" , 250.45)

t.see()
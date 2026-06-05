class Vehicle :

    def __init__(self , engine , type , seat) :
        
        self.engine = engine

        self.type = type

        self.seat = seat

        print("Parent Class Default Constructor is Called!!")

class Car(Vehicle) :

    def __init__(self , engine , type , seat) :

        super().__init__(engine , type , seat)

        print("Child Class Default Constructor is Called!!")

    def getCarInfo(self) :

        print("Engine..." , self.engine)

        print("Type..." , self.type)

        print("Seat..." , self.seat)

c = Car("V6" , "BGT" , 10)

c.getCarInfo()

c1 = Car("V3" , "BGM" , 15)

c1.getCarInfo()
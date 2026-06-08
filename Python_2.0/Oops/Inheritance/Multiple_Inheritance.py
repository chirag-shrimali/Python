'''
    A ------------ B
    --------------
    |  Multiple  |
    --------------
        |
        C
'''

class Father :

    city = "Ahmedabad"

    age = 45

    def __init__(self) :

        print("Father Class is Called!!")

        self.amount = 10000

        self.a = 10

class Mother :

    city = "Delhi"

    age = 42

    def __init__(self) :
        
        print("Mother Class is Called!!")

        self.amount = 20000

        self.b = 20
        
class Child(Father , Mother) :

    def __init__(self) :

        super().__init__()

    def getInfo(self) :

        print("Amount = " , self.amount)

        print("City = " , self.city)

        print("Age = " , self.age)

        print("A = " , self.a)

        # print("B = " , self.b) # Error occurs because it can not be find Mother Constructors...

c = Child()

c.getInfo()
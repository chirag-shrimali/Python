from abc import ABC , abstractmethod

class RBI(ABC) :

    def __init__(self) :
        
        print("Class RBI is Called!!")

    @abstractmethod
    def withdraw(self) :

        print("Withdraw from RBI")

    def loan() :

        print("Loan is Called!!")

class SBI(RBI) :

    def __init__(self) :

        print("Class SBI is Called!!")

        super().__init__()

    def withdraw1(self) :

        print("Withdraw from SBI")

s = SBI()

s.withdraw()
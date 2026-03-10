# Abstraction : which can be hidding the internal details of the users...

"""
Abstraction Class ---> from abc import ABC

Abstraction Methods ---> from abc import abstractclassmethod
"""

from abc import ABC , abstractclassmethod

class bank_account(ABC):
    def __init__(self,name):
        self.name=name
        self.__balance=0 
        
    @abstractclassmethod
    def deposit(self,amount):
        pass 
       
    @abstractclassmethod
    def withdraw(self,amount):
        pass 
    
    @abstractclassmethod
    def get_balance(self):
        pass 

    def display(self): 
        print(f"name:{self.name} balance:{self.__balance}")
        
class savings_account(bank_account):
    def __init__(self, name):
        super().__init__(name)
        self.accnumber =123456356
        self.__balance=0
        
    def deposit(self, amount):
        self.__balance+=amount
        print(f"deposited {amount} to {self.name}")
        
    def withdraw(self, amount):
        self.__balance-=amount
        print(f"withdraw {amount} from {self.name}")
        
    def get_balance(self):
        return self.__balance
    
a=savings_account("Chirag")
a.display()
print("your initial balance is  : ",a.get_balance())
a.deposit(25000)
a.withdraw(13000)
print("your final balance is  : ",a.get_balance())
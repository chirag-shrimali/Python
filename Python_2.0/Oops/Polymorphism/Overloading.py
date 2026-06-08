'''

Over - Loading :- Same Member Function name , but different arguments are given... 

E.x. int , int && int , int , int 

'''

class Bank :

    def __init__(self) :
        
        print("Bank Class is Called!!")

    def demo(self , a) :

        print("Method Overloading With Single Argument..." , a)

    def demo(self , a , b) :

        print("Method Overloading With Double Argument..." , a , b)

b = Bank()

b.demo(10 , 20)
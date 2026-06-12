'''

If students need to implement OOP concepts themselves, give projects where overloading, overriding, 
constructors, inheritance, etc. are naturally required.
1. Food Delivery App 🍔
Classes :
User
Restaurant
Order
Concepts:
Constructor → create user/order
Overriding → calculate_bill()
Normal Order
Premium Order
Overloading → add_item()
by item name
by item name + quantity

'''

class User :

    def __init__(self) :

        print("User Class is Called!!")

        self.name = "Chirag"

        self.amount = 500

class Restaurant(User) :

    def __init__(self):

        self.res = "Royal Restaurant"

        super().__init__()

    def show_name(self) :

        print(f"Restaurant Name is : {self.res}")

        print(f"User Name is : {self.name}")

        print(f"Amount is : {self.amount}")

class Order(Restaurant) :

    def __init__(self) :
        
        print("Order Class is Called!!")

        super().__init__()

    def add_item(self , name) :

        print(f"Item Name is : {name}")

    def add_item(self , name , quantity) :

        print(f"Item Name is : {name} and Quantity is : {quantity}")

o = Order()

o.show_name()

o.add_item("Punjabi Dish" , 2)
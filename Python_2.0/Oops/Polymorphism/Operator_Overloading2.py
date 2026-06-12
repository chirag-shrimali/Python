class Cart :

    def __init__(self , items) :
        
        self.items = items

    def __sub__(self, other) :
        
        print("Self..." , self.items)

        print("Other..." , other.items)

        total = self.items["amount"] - other.items["amount"]

        return total
    
c1 = Cart({"name" : "iphone" , "amount" : 12000})

c2 = Cart({"name" : "samsung" , "amount" : 13000})

final = c2 - c1

print(final)
def order_food(func) : # 3
    
    print(func) # func == address of throw_party # 4

    def inner() : # 7

        print('Ordering the Food!!') # 8

        func() # throw_party() function is called.. # 9

    return inner # 5

@order_food # Decorator can be makes...2 # 6 (control)

def throw_party() : # 10

    print("Throw Party Function is Called...") # 11

throw_party() # 1
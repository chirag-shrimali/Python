def smartDiv(func) : # func == div address

    def inner(x , y) :

        print("No1 Inside Inner..." , x)

        print("No2 Inside Inner..." , y)

        print("Smart Div Function is Called...")

        if y == 0 :

            print('We can not be divide the number by 0...')

        else :

            func(x , y) # div(a , b) function can be called...

    return inner

@smartDiv # Decorator is made...

def div(a , b) :

    print("Division of Two No are :" , a / b)

# div(15 , 5) # 3.0

div(15 , 0)
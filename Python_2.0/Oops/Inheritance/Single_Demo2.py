'''
    
    A(Parent Class)
    |
    B(Child Class , it can be inherited...)

'''

class Color :

    def hash(self) :

        print("\nI am Hash of any Color...")

        self.color = "FFFFFF"

class White(Color) :

    def show(self) :

        return self.color
    
w = White()

print(w.show())
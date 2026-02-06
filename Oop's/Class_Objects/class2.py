# Oop's :- Object Oriented Programming Langauge

# Private Visibility Of Scope :-

class Animal :
    __dog = "bhaw bhaw!!"
    __cat = "meow meow!!"
    __crow = "caw caw!!"

    print(__dog)

    # Create the Members Functions

    def show(self) :
        print(f"\nDog Speakes {self.__dog}")
        print(f"\nCat Speakes {self.__cat}")
        print(f"\nCrow Speakes {self.__crow}")

a = Animal()

# Not Accessible due to Private Scope Of Visibility

# print(a.__dog)

# print(a.__cat)

# print(a.__crow)

a.show()

# Not Update due to Private Scope Of Visibility so can't be access the data members thus no change can be occurs errors not come but changes also not occurs

print("\n--------------------------------------------------------------------")

a.__dog = "meow!!"

a.__cat = "caw!!"

a.__crow = "bhaw!!"

a.show()
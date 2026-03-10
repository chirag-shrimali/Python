# Abstractions which can be hidding the data from the users...

''' 
abtraction : means hiding internal implementations detalis and showing only essential features to the user. 

1. abstract class : from abc import ABC  ==> abc ==> abstract base class
 
2. abstract method : @abstractmethod ==> abstract method
'''

from abc import ABC , abstractclassmethod

class animal(ABC) :
    @abstractclassmethod
    def sound() :
        pass

class dog(animal) :
    def sound(self) :
        print("\nThe Dog Says Bhaw Bhaw!!")

class cat(animal) :
    def sound(self) :
        print("\nThe Cat Says Meow Meow!!")

class bird(animal) :
    def sound(self) :
        print("\nThe Bird Says Tweet Tweet!!")

d = dog()

d.sound()

c = cat()

c.sound()

b = bird()

b.sound()
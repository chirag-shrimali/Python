# Base Class
class Vehicle:
    def __init__(self, brand, speed):
        self.__brand = brand
        self.__speed = speed

    # Getter Methods
    def get_brand(self):
        return self.__brand

    def get_speed(self):
        return self.__speed

    # Setter Methods
    def set_brand(self, new_brand):
        self.__brand = new_brand

    def set_speed(self, new_speed):
        self.__speed = new_speed

    def start_engine(self):
        print("Vehicle engine is starting...")

    # Overloading using default argument
    def accelerate(self, speed=None):
        if speed is None:
            self.__speed += 10
        else:
            self.__speed += speed
        print(f"New Speed: {self.__speed}")


# Derived Class Car
class Car(Vehicle):
    def __init__(self, brand, speed, color):
        super().__init__(brand, speed)
        self.__color = color

    def get_color(self):
        return self.__color

    def set_color(self, new_color):
        self.__color = new_color

    # Overriding
    def start_engine(self):
        print("Car engine starts with a key 🔑")


# Derived Class Bike
class Bike(Vehicle):
    def __init__(self, brand, speed):
        super().__init__(brand, speed)

    # Overriding
    def start_engine(self):
        print("Bike engine starts with a self button 🏍️")


# Polymorphism
vehicles = [
    Car("Toyota", 150, "White"),
    Car("Honda", 200, "Red"),
    Bike("Yamaha", 120),
    Bike("Suzuki", 140)
]

for v in vehicles:
    v.start_engine()     # Polymorphism
    v.accelerate()       # Without argument
    v.accelerate(20)     # With argument
    print()
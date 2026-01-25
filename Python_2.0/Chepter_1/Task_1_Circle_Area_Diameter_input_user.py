# Task is to find the Area of the circle in which the diameter can be enters by user as input() function

diameter = int(input("Enter the Diameter of the Circle : "))

radius = diameter / 2

area = 3.14 * radius * radius  
# area = 3.14 * (radius ** 2)

print("\nThe Diameter of the Circle which can be enter by user is :",diameter,"meter")

print("\nThe Area of the Circle are :",area,"meter2")
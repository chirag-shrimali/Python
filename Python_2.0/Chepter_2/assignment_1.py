# Smart Temperature Converter

"""
Take the input in Celsius and print it's equivalent in Fahrenheit and Kelvin.
(Use Explicit type conversion and the arithmetic operators.)

Formula :

Fahrenheit = (C X 9/5) + 32

Kelvin = C + 273.15
"""

celsius = float(input("Enter the Value of the temperature in the Celsius : "))

Fahrenheit = (celsius * 1.8) + 32

Kelvin = celsius + 273.15

print("\nThe Value of the Celsius is in the Fahrenheit are :",Fahrenheit)

print("\nThe Value of the Celsius is in the Kelvin are :",Kelvin)
# The floor slope

"""
Problem Description:

Given the (x, y) co-ordinates of two points on a 2D plane, calculate the slope of the line they make 
and print the greatest integer less than of equal to the value of the slope acoording to the output 
format specified.

Input:

1 
2 
3 
4 

Output:

The value of the floor slope is 1
"""

print('\n----------We are finding the Floor of Slope of 2D-Plane----------\n')

x1 = int(input("Enter the first lines that contains the x_1 coordinate : "))
y1 = int(input("Enter the first lines that contains the y_1 coordinate : "))
x2 = int(input("Enter the first lines that contains the x_2 coordinate : "))
y2 = int(input("Enter the first lines that contains the y_2 coordinate : "))

slope = (y2 - y1) // (x2 - x1)

print("\nThe value of the floor slope is :",slope)
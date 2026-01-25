# Nilay only likes Integers

"""
Problem Description: 
Nilay is continuously receiving a stream of numbers that are rounded off to three decimal places. The 
program that Nilay wrote is giving the output in form of a float, but he needs this output in form of 
an integer. This integer here will be the largest integer less than or equal to the given number. Write 
a program that helps Nilay solve this problem.

Input: 

0.001 
16.203 
20.999 

Output: 

0
16 
20
"""

print("\n----------Wake up to Reality----------\n")

f1 = float(input('Enter the First Floating Value : '))
f2 = float(input('Enter the Second Floating Value : '))
f3 = float(input('Enter the Third Floating Value : '))

print("\n------------------------------------------\n")

print(int(f1))
print(int(f2))
print(int(f3))
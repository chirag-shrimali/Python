# sum of all the probabilities should be always 1

"""
Problem Description: 

One of the most fundamental axioms of probability theory is that the total probability of a set of 
related events always adds up to 1. Given three probability values, your task is to check if they all add 
up to 1.

Input:

0.70 
0.20 
0.10 

Output: 

True
"""

ev1 = float(input("Enter the First events probabilities : "))
ev2 = float(input("Enter the Second events probabilities : "))
ev3 = float(input("Enter the Third events probabilities : "))

sm = ev1 + ev2 + ev3

if round(sm , 1) == 1.0 :
    print('True')
else :
    print("False")
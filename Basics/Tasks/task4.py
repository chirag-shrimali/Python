# Problem Description: Given two names A and B as input, print "A says Hi to B", where A and B are the names in input.

"""
Problem Constraints 
1 <= len(A), len(B) <= 15

Examples  
Input: 
Ram 
Shyam 
Output: 
Ram says Hi to Shyam
"""

dost1 = input('Enter the Dost 1 Name : ')
dost2 = input('Enter the Dost 2 Name : ')

if(len(dost1) >= 1 and len(dost2) <= 15) :
    print(f"{dost1} says Hi to {dost2}")
else :
    print('Length of your Username contains the Invalid conditions!!')
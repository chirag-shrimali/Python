# The total savings, the amount of money before exchange and the exchanging amount, denoting the amount of money that is spent from the savings. 

"""
Problem Description: 
Your friend Rahul plans to visit exotic countries all around the world. Sadly, Rahul's math skills aren't 
good enough. Given the amount of money Rahul has before the currency exchange and the amount 
of money that is spent from his savings, print the amount of money that remains in his savings.

Problem Constraints: 
1 <= N <= 1000 
1 <= M <= N

Examples :-

Input: 

116 
12 

Output: 

104
"""

total_savings = int(input("Enter the the total savings, the amount of money before exchange : "))
ex_amount = int(input("Enter the exchanging amount, denoting the amount of money that is spent from the savings : "))

range1 = 1 <= total_savings <= 1000
range2 = 1 <= ex_amount <= total_savings

amt_money = total_savings - ex_amount

if range1 and range2 :
    print("\nThe amount of money that is left in his savings are :",amt_money)
else :
    print('\nInvalid amount that you write!! So,write a valid amount...')
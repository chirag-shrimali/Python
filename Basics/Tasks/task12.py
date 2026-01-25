# writes a current date month and year as date(day)/month/year

"""
Problem Description: 

Rahul is working on solving a problem that needs him to have his date in Day/Month/Year format. 
Unfortunately, he just has the Day, Month, and Year as an integer value. Write a piece of code that 
helps Rahul get out of this situation.

Input:

1 
12 
2017 

Output: 

1/12/2017
"""

day = int(input('\nEnter the Date(day) : '))
month = int(input("Enter the Month : "))
year = int(input('Enter the Year : '))

print(f"\nThe Date is : {day}/{month}/{year}")
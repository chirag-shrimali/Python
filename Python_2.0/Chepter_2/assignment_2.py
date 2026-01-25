# Bill Split Calculator

'''
Write a Program that takes the total bill amount and number of friends as input.
Calculate how much each person will pay.
Also print the data type of each variable used.

(Hint : use float() and division operator)
'''

total_bill_amount = float(input("\nEnter the Total Amount of Bill : "))

print(type(total_bill_amount)) # <class 'float'>

no_friends = float(input("\nEnter the number of friends : "))

print(type(no_friends)) # <class 'float'>

pay_each_person = total_bill_amount/no_friends

print("\nThe Amount of Bill that each person will be pay is :",pay_each_person)

print(type(pay_each_person)) # <class 'float'>
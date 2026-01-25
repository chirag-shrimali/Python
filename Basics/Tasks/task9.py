# Total Bills Value

'''
Problem Description: 
Given the value of a single bill and the number of bills you received, print the total value of the bills. 

Note: The value of all the bills are same 

Problem Constraints 
1 <= N <= 100 
1 <= M <= 100
'''

print("\n\t\t----------Total Bills Value----------\n")

single_bill = int(input('Enter a Single Bill Value : '))
no_bill = int(input('Enter the number of Bills that you have been received : '))

range1 = 1 <= single_bill <= 100
range2 = 1 <= no_bill <= 100

total_value_of_bills = single_bill * no_bill

if(range1 and range2) :
    print("\nThe Total Value of the Bills are :",total_value_of_bills)
else :
    print("\nInvalid Values!! Write a valid numbers of values for bills...")
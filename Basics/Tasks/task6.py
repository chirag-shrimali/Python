# Remaining Bake Time

"""
Problem Description: 
You're going to write some code to help you cook a gorgeous lasagna from your favorite cookbook. 
According to your cookbook, the Lasagna should be in the oven for 40 minutes. Given the time (in 
minutes), the lasagna has been in the oven, find how many more minutes the lasagna still needs to 
bake for.

Problem Constraints 
0 <= N <= 40

Examples 
Input:  
30 
Output:  
10
"""

print('\n******* We are going to find Remaining Bake Time(in minutes) for cook a gorgeous lasagna!! *******\n')

n = int(input('Enter the actual time (in minutes) the lasagna has been in the oven for : '))

range = 0 <= n <= 40

if(range) :
    print("\nTotal Remaining Bake Time for cook a gorgeous lasagna is :",40 - n)
elif n < 0 :
    print("\nInvalid Numbers negative numbers are not allow here...")
else :
    print('\nI think you have no knowledge about mine policy because here clearly written that range could be in 0 to 40 but you write more than it so write in the range of it...')
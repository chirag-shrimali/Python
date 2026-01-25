# Total Elapsed Cooking Time

'''
Problem Description: 
You wrote some code to help you cook a gorgeous lasagna from your favorite cookbook. Now, you 
want to find the total number of minutes you've been cooking for the sum of your preparation time 
and the time the lasagna has already spent baking in the oven. The preparation time of one layer is 2 
minutes. Given the number of layers added to the lasagna and the number of minutes the lasagna 
has been baking in the oven, find the total elapsed cooking time (prep + bake) in minutes. 
Problem Constraints:

1 <= N <= 20 
0 <= M <= 40
'''

print('\n******* We are going to find Remaining total elapsed cooking time (prep + bake) in minutes for cook a gorgeous lasagna!! *******\n')

no_layers = int(input('Enter the numbers of Layers for cook a gorgeous lasagna : '))
time_lasagna = int(input("Enter the time the lasagna has already spent baking in the oven : "))

# The preparation time of one layer is 2

preparation_time = no_layers * 2 # in minutes

range1 = 1 <= no_layers <= 20
range2 = 0 <= time_lasagna <= 40
final_answer = preparation_time + time_lasagna

if(range1 and range2) :
    print("\nThe total elapsed cooking time for cook a gorgeous lasagna is :",final_answer)
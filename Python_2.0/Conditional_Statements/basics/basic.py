# basic program of the conditional statements

# age = int(input("\nEnter Your Age : "))

# if(age >= 18) :
#     print("\nYou can give the vote,because you are eligible for the giving the vote...")
# elif age <= 0 :
#     print("\nYou are come from the different planets because your age is negative that's not possible in earth...")
# else :
#     print("\nYou can not give the vote, because you are not eligible for the giving the vote...")

# print('\nEnd of the Code')

# --------------------------------------------------------------------------------------------------------

light = input("\nEnter the light signal color : ")

if(light.lower() == "red") :
    print('\nStop') # indentation in python 4 spaces
elif light.lower() == 'green' :
    print("\nGo")
elif light.lower() == "yellow" :
    print("\nSlow down")
else :
    print("\nThe Light Signal may be broken...")
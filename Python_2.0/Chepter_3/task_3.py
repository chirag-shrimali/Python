# Write a Program that :-

'''
1. Takes a Sentence as input
2. Converts it into a LowerCase
3. Replaces all spaces " " With underscores "_"
4. Prints the new String
'''

sen = input("\nEnter the Sentences : ")

low_case = sen.lower()

replace = low_case.replace(' ' , "_")

print("\nThe Changed Sentences are :",replace)
# task : 2 :- 

"""
Write a python program that take one input string and in output count the no of words,
Find No of letters in String,Find the longest word in the String.

For Example:-
Input:-This is the python program
Output:-No of Words = 5
	    No of letters = 26(including whitespace)
	    Longest Word = program
"""

input = "This is the python program"

# for the words-------------------------------------------------

space = input.count(" ")

print("\nNo of Words :",space + 1)

# for the letters-------------------------------------------------

length = len(input)

print("\nNo of letters :",length)

# for the longest word-------------------------------------------

sp = input.split()

print() # for the new line prints

print(sp)
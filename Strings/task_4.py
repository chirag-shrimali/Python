"""
task : 10 
	Write a Python program to find the length of a given list of non-empty strings.
	Input:
	['cat', 'car', 'fear', 'center']
	Output:
	[3, 3, 4, 6]
	Input:
	['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
	Output:
	[3, 3, 7, 5, 2, 4, 0]
"""

input = ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']

print("\nInput :",input)

list = []

for i in input :
    list.append(len(i))
    
print("\nOutput :",list)
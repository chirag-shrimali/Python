# Problem Description: Given a name A as input. Print "Hello A", where A is the name in input.
"""
Problem Constraints:

1 <= len(A) <= 15 
Characters in A are in lowercase English Alphabets.

Examples
Input 1: 
Ram 
Output 1: 
Hello Ram 
"""

username = input('Enter the Username : ')

if(len(username) > 0 and len(username) <= 15) :
    print(f"Hello {username}")
else :
    print("Your UserName is too Big!! Write username between 1 to 15 characters only...")
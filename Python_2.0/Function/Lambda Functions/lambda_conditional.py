# Lambda With Conditional Statements...

'''
1.

x = lambda x : "Even" if x % 2 == 0 else "Odd"

# print(x(2)) # Even

print(x(3)) # Odd

'''

# ------------------------------------------------------------------------------------

"""
2.

x = lambda name : "Palindrome" if name == name[ : : -1] else "Not Palindrome"

print(x("Chirag")) # Not Palindrome

ans = x("madam")

print(ans) # Palindrome

"""

# ------------------------------------------------------------------------------------

x = lambda a , b : a if a > b else b

print(x(1 , 20)) # 20

ans = x(24 , 1)

print(ans) # 24
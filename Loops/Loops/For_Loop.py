# Types of Loops :-
'''
1. For Loop -> Entry Controlled Loop
2. While Loop -> Exit Controlled Loop
'''

# Printing First 1 to 5 numbers using for loops

'''
print(1)
print(2)
print(3)
print(4)
print(5)
'''

# Syntax of For Loop is for variable_name in range(start , end(stop) , step_size(increament/decreament))

# here in the range of 1 to 6 --- 1 can be included and 6 excluded as n - 1
# for i in range(1 , 6) :
#     print(i)

# Printing 1 to 100

# for i in range(1 , 101) :
#     print(i,end = " ")

for i in range(5) : # by default in the for loop range starts with 0 to 5 means , prints 0 to 4 => 0 as included and 5 as excluded  
    print(i)
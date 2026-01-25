# prints the following patterns :-

"""
        columns
           |
rows->  * * * * * -> i = 1
        *       *
        *       *
        *       *
        * * * * * -> i = 5
"""

no = int(input('Enter the No : '))

for i in range(1 , no + 1) :
    for j in range(1 , no + 1) :
        if i == 1 or i == no or j == 1 or j == no :
            print('*' , end=" ")
        else :
            print(' ' , end=" ")
    print()

# no = int(input('Enter the No : '))

# for i in range(1 , no + 1) :
#     if i == 1 or i == no :
#         print('*' * (no) , end="")
#         print()
#     else :
#         print("*", end="")
#         print(' ' * (no - 2) , end="")
#         print("*", end="")
#         print()
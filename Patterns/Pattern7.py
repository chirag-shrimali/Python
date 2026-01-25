# Prints the following patterns :-

"""
     column
        |
rows -> 5 4 3 2 1 -> i = 5
        5 4 3 2 -> i = 4
        5 4 3 -> i = 3
        5 4 -> i = 2
        5 -> i = 1
"""

no = int(input("Enter the No : "))

for i in range(1, no + 1) :
    for j in range(5 , i - 1 , -1) :
        print(j,end=" ")
    print("")
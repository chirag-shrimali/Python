# Prints the following patterns :-

"""
     column
        |
rows -> 1 2 3 4 5 -> i = 5
        2 3 4 5 -> i = 4
        3 4 5 -> i = 3
        4 5 -> i = 2
        5 -> i = 1
"""

no = int(input("Enter the No : "))

for i in range(no , 0 , -1) :
    for j in range(no - i + 1 , no + 1) :
        print(j,end=" ")
    print("")
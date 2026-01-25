# Prints the following patterns :-

"""
     column
        |
rows -> 1 2 3 4 5 -> i = 5
        1 2 3 4 -> i = 4
        1 2 3 -> i = 3
        1 2 -> i = 2
        1 -> i = 1
"""

no = int(input("Enter the No : "))

for i in range(no , 0 , -1) :
    for j in range(1 , i + 1) :
        print(j,end=" ")
    print("")
# prints the following patterns :-

"""
     column
        |
rows -> a -> i = 1
        a b -> i = 2
        a b c -> i = 3
        a b c d -> i = 4
        a b c d e -> i = 5
"""

# ascii value of a -- 97 , b -- 98 , c -- 99 , d -- 100 , e -- 101

no = int(input("Enter the No : "))

for i in range(1 , no + 1) :
    for j in range(1 , i + 1) :
        print(chr(j + 96),end=" ")
    print("")
    
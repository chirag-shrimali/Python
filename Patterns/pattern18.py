# prints the following patterns :-

"""
    columns
       |
rows-> * * * * * -> i = 5
       *     * -> i = 4
       *   * -> i = 3
       * * -> i = 2
       * -> i = 1
"""

no = int(input('Enter the No : '))

for i in range(no , 0 , -1) :
    for j in range(1 , no + 1) :
        if i == no or i == j or j == 1 :
            print('*' , end=" ")
        else :
            print(' ' , end=" ")
    print()
# prints the following patterns:-

"""
        columns
            |
rows->      * -> i = 1
          * * -> i = 2
        * * * -> i = 3
      * * * * -> i = 4
    * * * * * -> i = 5
"""

no = int(input('Enter the No : '))

for i in range(1 , no + 1) :
    print(' ' * (no - i) , end="")
    print('*' * (i) , end="")
    print()

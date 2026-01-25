# prints the following patterns :-

'''
    columns
       |
rows-> * * * * * -> i = 5
         * * * * -> i = 4
           * * * -> i = 3
             * * -> i = 2
               * -> i = 1
'''

no = int(input('Enter the No : '))

for i in range(no , 0 , -1) :
    print('*' * (i) , end=' ')
    print()
    print(' ' * (no - i) , end=" ")
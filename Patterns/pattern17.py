# prints the following patterns :-

'''
    columns
        |
rows -> * -> i = 1         
        * *  -> i = 2   
        *   *  -> i = 3
        *     *  -> i = 4   
        * * * * * -> i = 5
'''

no = int(input('Enter the No : '))

for i in range(1 , no + 1) :
    for j in range(1 , no + 1) :
        if i == no or i == j or j == 1 :
            print('*' , end=" ")
        else :
            print(' ' , end=" ")
    print()
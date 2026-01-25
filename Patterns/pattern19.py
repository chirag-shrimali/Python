# prints the following patterns :-

'''
rows -> *
       *  *
      *    *
     *      *
    *        *
     *      *
      *    *
       *  *
        *
'''

no = int(input('Enter the No : ')) # 5

for i in range(1 , no + 1) : # 1 to 6 -> 1 2 3 4 5
    for k in range(no , i , -1) : # 5 to 1 -> 5 4 3 2 
        print(' ' , end="")
    for j in range(1 , i + 1) : # 1 to 2
            if(i == 1 or j == 1 or i == j) :
                print('*' , end=" ")
            else :
                print(" " , end=" ")
    print()
for i in range(no - 1 , 0 , -1) : # 4 to 0 -> 4 3 2 1
    for k in range(1 , no - i + 1) : # 1 to 2 -> 1 
        print(' ' , end="")
    for j in range(1 , i + 1) : # 1 to 2
            if(i == 1 or j == 1 or i == j) :
                print('*' , end=" ")
            else :
                print(" " , end=" ")
    print()
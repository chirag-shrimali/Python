# print the star pattern

'''
***
* *
***
'''

no = int(input("Enter the No : "))

for i in range(1 , no + 1) :
    if(i == 1 or no == i) :
        print("*" * (no) , end="")
    else :
        print("*",end="")
        print(" " * (no - 2) ,end="")
        print("*",end="")
        # print("")
    print("")
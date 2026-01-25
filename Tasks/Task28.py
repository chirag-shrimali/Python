# print a Multiplication table of n using for loops in reversed order

no = int(input("Enter the Number that you want it's Multiplication Table : "))

for i in range(10 , 0 , -1) :
    print(no , "X" , i , "=" , no * i)

# for i in range(1 , 11) :
#     print(f"{no} X {11 - i} = {no * (11 - i)}")
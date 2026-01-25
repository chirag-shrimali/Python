# Multiplication table of a given number using for loop

no = int(input("Enter the Number that you want it's Multiplication Table : "))

for i in range(1 , 11) :
    print(no,"X",i,"=",no * i)
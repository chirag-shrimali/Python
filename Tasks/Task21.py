# Multiplication Table the number that user enters using while loop

no = int(input("Enter the Number that you want it's Multiplication Table : "))

i = 1
while(i < 11) :
    print(no,"X",i,"=",no * i)
    i += 1 # i = i + 1
# nesting if condition statements

a = int(input("\nEnter the Value of A : "))

b = int(input("\nEnter the Value of B : "))

c = int(input("\nEnter the Value of C : "))

if(a > b) :
    if(a > c) :
        print("\nA is Greater...")
    else :
        print("\nC is Greater...")
else :
    if(b > c) :
        print("\nB is Greater...")
    else :
        print("\nC is Greater...")
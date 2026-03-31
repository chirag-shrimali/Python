# pass 5 numbers in the args and return the sum of that numbers...

# The Data Type of Args is Tuples...

def getNoSum(*args) :

    sum = 0

    for i in args :
        sum = sum + i # sum += i

    print(f"The No is : {args}")

    print(f"The Sum is : {sum}")

getNoSum(1 , 2 , 3 , 4 , 5)
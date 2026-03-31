# 2. accept list as argument and return sum of list  dont use builtin sum function..

def getList(items) :
    
    sum = 0

    for i in items :
        sum = sum + i # sum += i

        print(i)

    return sum

print(f'The Sum is : {getList([1 , 2 , 3 , 4])}')
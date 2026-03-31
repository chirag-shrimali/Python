# pass 3 arguments in args and check all arguments must be int only if yes return true else false...

def getArgu(*args) :

    for i in args :
        if type(i) != int :
            print('False')
            break
    else :
        print('True')

    print(f"The Arguments are : {args}")

# getArgu(1 , "Chirag" , True , 21.45)

# getArgu(1 , 25 , True , 21)

getArgu(1 , 25 , 49 , 21)
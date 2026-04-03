# calc("+" , 10 , 20 , 30 , 40 , 50) # args

def calc(*args) :
    print(args)

    choice = args[0]

    match choice :
            case '+' :
                sum = 0

                for i in args[1 : ] :
                    sum += i
                print(sum)

            case '-' :
                sum = args[1]
                for i in args[2 : ] :
                    sum -= i
                print(abs(sum))

# calc("+" , 10 , 20 , 30 , 40 , 50 , 60) # 210

calc("-" , 10 , 20 , 30 , 40 , 50 , 60)
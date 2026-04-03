"""

checkData(name = "Chirag" , city = "ahmedabad" , ...)

values data type if string return 'True' else 'False'...

"""

def checkData(**kwargs) :
    
    ch = kwargs.values()

    for i in ch :
        if type(i) != str :
            print("False")
            break
    else :
        print('True')

    print(kwargs)

# checkData(name = "Chirag" , city = "Delhi" , state = "Gujarat") # True

checkData(name = "Chirag" , city = "Delhi" , state = "Gujarat" , age = 19) # False
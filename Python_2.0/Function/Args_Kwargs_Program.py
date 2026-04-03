def getData(**kwargs) :

    print(kwargs)

    for i in kwargs.values() :
        if not isinstance(i , str) :
            print('False')
            break

    else :
        print('True')

getData(name = "Chirag" , city = "Gujarat" , state = "ahmedabad") # Valid --> True

# getData(name = "Chirag" , city = "Gujarat" , state = "ahmedabad" , salary = 15000) # False

# -----------------------------------------------------------------------

# def checkData(**kwargs):
#     for i in kwargs.values():
#         # if type(i)!= str:
#         #     return False
#         if not isinstance(i,str):
#             print('False')
#             break
#     else :
#         print('True')

# checkData(name = "Chirag" , city = "Gujarat" , state = "ahmedabad")
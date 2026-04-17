def loginRequired(func) :

    def inner(*args , role) :

        if role in args :

            print('Authoried Access...')

            func(args , role = role)

        else :

            print('Unauthorized Access...')

    return inner

@loginRequired # make the decorator

def accessHomePage(*args , role) :

    print('Accessed the Home Page and the Role is :' , role)

accessHomePage("User" , "Admin" , "Manager" , role = "Manager")

# accessHomePage("User" , "Admin" , "Manager" , role = "manager")

# accessHomePage("User" , "Admin" , "Manager" , role = "Chirag")

print('----------------------------------------------------------')

@loginRequired

def accessCartPage(*args , role) :

    print("Accessed the Cart Page and the Role is :" , role)

accessCartPage("User" , "Admin" , role = "Admin")

# accessCartPage("User" , "Admin" , role = "Manager")
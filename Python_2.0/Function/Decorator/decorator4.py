def loginRequired(func) :

    def inner(role) :

        print("Inner Function is Called...")

        if role == 'Admin' :

            func(role)

        else :

            print('Unauthorized...')

    return inner

@loginRequired
def accessData(role) :

    print('Accessing the data and my role is :' , role)

accessData('Admin')

# accessData('User')

@loginRequired
def accessFiles(role) :

    print('Accessing the Files and my role is :' , role)

accessFiles('Admin')

# accessFiles('User')
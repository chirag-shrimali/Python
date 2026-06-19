from CustoumEx import StringError

name = "madama"

try :

    if name != name[ : : -1] :

        raise StringError("Name is not a Palindrome!!")
    
except StringError as s :

    print(s)

except ValueError as v :

    print("ValueError..." , v)
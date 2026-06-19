from CustoumEx import StringError

email = "chirag@0411gmail.com"

try :

    if '@' not in email :

        raise StringError("Email is not a Valid!!")
    
    print("Email..." , email)

except StringError as s :

    print("StringError..." , s)

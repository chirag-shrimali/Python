"""
ask user to create password  condition :
    
    1.password len ==> min 8
    2.1 upper case 1 lower case 1 digit 1 special char
    
example :
    password : moksh1211   ==> wrong  ==> special char, upper  
    
    password : Moksh1211   ==> wrong  ==> special char 
    password : Moksh1211!  ==> correct
   
hint : isdigit() , islower() ,isupper() , isalpha() , isalnum()
"""

print("\n---------------PASSWORD VALIDATION---------------")

password = input("\nEnter the Password : ")

lower = False
upper = False
digit = False
special = False

if(len(password) < 8) :
    print("\nInvalid Password!!")
else :
    for i in password :
        if(i.isupper()) :
            upper = True
        elif(i.islower()) :
            lower = True
        elif(i.isdigit()) :
            digit = True
        elif(not i.isalnum()) :
            special = True

    if(lower and upper and digit and special) :
        print("\nCorrect Password!!")
    else :
        print("\nWrong Password because:")

        if(not lower) :
            print("At least one Lower_Case is Required")
        if(not upper) :
            print("At least one Upper_Case is Required")
        if(not digit) :
            print("At least one Digit is Required")
        if(not special) :
            print("At least one Special Character is Required")
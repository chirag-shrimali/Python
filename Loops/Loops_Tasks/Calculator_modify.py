print("\n\t\t\t\t----------Welcome to the Chirag's Calculator----------\n")
no1 = int(input('Enter the No1 : '))
no2 = int(input("Enter the No2 : "))

while(1) :
    print('\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Remainder\n6. Power\n7. Exit')
    choice = int(input("Enter Your Choice : "))
    if(choice > 0 and choice < 7) :
            match choice :
                case 1 :
                    add = no1 + no2
                    print("\nAddition :",add)

                case 2 :
                    sub = no1 - no2
                    print("\nSubtraction :",sub)

                case 3 :
                    mul = no1 * no2
                    print("\nMultiplication :",mul)

                case 4 :
                    div = no1 / no2
                    print("\nDivision :",div)

                case 5 :
                    rem = no1 % no2
                    print("\nRemainder :",rem)

                case 6 :
                    power = pow(no1 , no2)
                    print("\nPower :",power)

    elif choice == 7 :
            print('\nExiting Successfully!!!')
            break

    elif(choice <= 0) :
            print('\nInvalid Choice of Selection.So,select the valid choice of selection...')

    elif(choice > 7) :
         no1 = int(input('\nEnter the New No1 : '))
         no2 = int(input("Enter the New No2 : "))
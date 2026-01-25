print("\n########## WELCOME TO THE SIMPLE PYTHON CALCULATORS ##########")
print("\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus\n6.Power")

choice = int(input("Enter Your Choice (1-5) : "))

a = int(input("\nEnter the No1 : "))
b = int(input("\nEnter the No2 : "))

add = a + b
sub = a - b
mul = a * b
div = a / b
mod = a % b
power = pow(a ,b)

match choice :
    case 1: print("\nAddition :",add)

    case 2: print("\nSubtraction :",sub)

    case 3: print("\nMultiplication :",mul)

    case 4: print("\nDivision :",div)

    case 5: print("\nModulus :",mod)

    case 6: print("\nPower :",power)
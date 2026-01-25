print("\n-------------------- ROYAL KID BANK --------------------\n")

print("*****Create Account*****")

balance = 0

username = input("\nEnter the UserName : ")
password = input("\nEnter the Password : ")

def login(balance):
    username1 = input("\nEnter the Valid UserName : ")
    password1 = input("\nEnter the Valid Password : ")

    if(username1 == username and password == password1):
        print("\nLogin Successfully!!")
        balance = 25000
        print(f"\nYour Account has deposit {balance} balance...")
    else:
        print("\nInvalid Password or Username!! Pls, Enter a Valid Password or Username...")
    
    return balance

def deposit(balance):
    dep_money = int(input("\nEnter the amount of money that you want to Deposit : "))
    
    balance = balance + dep_money
    
    print(f"\nYour account has deposited {dep_money} and now balance is {balance}...")
    return balance

def withdraw(balance):
    withdraw_money = int(input("\nEnter the amount of money that you want to Withdraw : "))
    
    if(balance - withdraw_money >= 10000) :
        balance = balance - withdraw_money # balance -= withdraw_money
        print(f"\nYour account has withdrawn {withdraw_money} and now balance is {balance}...")
        return balance
    else :
        print("\nInsufficient Balance!!")
        return balance

def check_balance(balance):
    print(f"\nYour Current Bank Account having {balance} balance money...")

while True:
    print("\n1. Login\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Exit")

    choice = int(input("\nEnter the Choice (1-5) : "))

    match(choice):
        case 1:
            balance = login(balance)
            
        case 2:
            balance = deposit(balance)

        case 3:
            balance = withdraw(balance)

        case 4:
            check_balance(balance)

        case 5:
            print("\nExiting Successfully!!")
            break
class Bank:
    bank_account = 9876543210
    acc_holder_name = "Chirag Shrimali"
    balance = 50000
    pin_code = 7896

    def __init__(self):
        self.logged_in = False   # Login status

    def login_account(self):
        account = int(input("\nEnter the Bank Account No : "))
        name = input("\nEnter the Account Holder Name : ")

        if(self.bank_account == account and self.acc_holder_name == name):
            print("\nLogin Successfully!!")
            self.logged_in = True
        else:
            print("\nInvalid Account Information")

    def info(self):
        if not self.logged_in:
            print("\nPlease login first!")
            return

        print("\n============= BANK ACCOUNT INFORMATION =============")
        print("\nThe Bank Account is :", self.bank_account)
        print("\nThe Account Holder Name is :", self.acc_holder_name)
        print("\nThe Current Balance are :", self.balance)
        print("\n====================================================")

    def deposit(self, amt):
        if not self.logged_in:
            print("\nPlease login first!")
            return

        pin = int(input("\nEnter the Correct Pin No : "))

        if(self.pin_code == pin):
            self.balance += amt
            print("\nThe Deposit Money are :", amt)
            print("\nThe Current Balance are :", self.balance)
        else:
            print("\nInvalid Pin Code Number...")

    def withdraw(self, amt):
        if not self.logged_in:
            print("\nPlease login first!")
            return

        pin = int(input("\nEnter the Correct Pin No : "))

        if(self.pin_code == pin):
            if self.balance - amt >= 10000:
                self.balance -= amt
                print("\nThe Withdraw Money are :", amt)
                print("\nThe Current Balance are :", self.balance)
            else:
                print("\nInsufficient Balance!!")
        else:
            print("\nInvalid Pin Code Number...")

    def check_balance(self):
        if not self.logged_in:
            print("\nPlease login first!")
            return

        print("\nThe Current Balance are :", self.balance)

    def menu_driven(self):
        while True:
            print("\n1. Login")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Check Balance")
            print("5. Show Details")
            print("6. Exit")

            choice = int(input("\nEnter the Choice (1 - 6) : "))

            match choice:
                case 1:
                    self.login_account()
                case 2:
                    amt = int(input("Enter amount: "))
                    self.deposit(amt)
                case 3:
                    amt = int(input("Enter amount: "))
                    self.withdraw(amt)
                case 4:
                    self.check_balance()
                case 5:
                    self.info()
                case 6:
                    print("\nExiting Successfully!!")
                    break


b = Bank()
b.menu_driven()
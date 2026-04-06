def paytm(amt) :
    
    print("Pay Via Paytm...",amt)

def phonepay(amt) :

    print("Pay Via PhonePay...",amt)

def gpay(amt) :

    print("Pay Via Gpay...",amt)

def paynow(a , amt) :

    print("Paynow Function is Called...")

    a(amt)

userChoice = input("Enter Your Choice : ")

amt = int(input("\nEnter the Amount : "))

if userChoice == "paytm" :

    paynow(paytm , amt)

elif userChoice == "phonepay" :
    
    paynow(phonepay , amt)

elif userChoice == "gpay" :
    
    paynow(gpay , amt)
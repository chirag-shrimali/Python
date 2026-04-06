def paytm() :
    
    print("Pay Via Paytm...")

def phonepay() :

    print("Pay Via PhonePay...")

def gpay() :

    print("Pay Via Gpay...")

def paynow(a) :

    print("Paynow Function is Called...")

    a()

userChoice = input("Enter Your Choice : ")

if userChoice == "paytm" :

    paynow(paytm)

elif userChoice == "phonepay" :
    
    paynow(phonepay)

elif userChoice == "gpay" :
    
    paynow(gpay)
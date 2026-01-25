# Checking that enters a numbers by users is palindrome or not

no = int(input("Enter the No : "))

digit = len(str(no))

rev = 0

dup = no

# 0 to digit
for i in range(digit) :
    rem = dup % 10
    rev = (rev * 10) + rem
    dup = dup //10 # dup //= 10

if rev == no :
    print(no,"is a Palindrome No...")
else :
    print(no,'is not a Palindrome No...')
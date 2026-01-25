# Converts the numbers in the reverse

no = int(input("Enter the No : "))

rev = 0

digit = len(str(no))

for i in range(digit) :
    rem = no % 10
    rev = (rev * 10) + rem
    no = no//10

print(rev)
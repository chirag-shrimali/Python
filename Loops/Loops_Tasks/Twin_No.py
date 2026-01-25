# Checking that a numbers users enters is twin number or not

no = int(input("Enter the No : "))

digit = len(str(no))

sum = 0
mul = 1 # fc = 1
temp = no
for i in range(digit) :
   rem = no % 10
   sum = sum + rem # sum += rem
   mul = mul * rem # mul *= rem
   no = no//10

if sum == mul :
   print(temp,"is a Twin No...")
else :
   print(temp,'is not a Twin No...')
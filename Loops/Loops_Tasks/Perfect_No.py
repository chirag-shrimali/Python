# Checking that a number enters by users is perfect or not

no = int(input("Enter the No : "))

sum = 0

for i in range(1 , no) :
    if(no % i == 0) :
        sum = sum + i # sum += i

if no == sum :
    print(no,'is a Perfect No...')
else :
    print(no,"is not a Perfect No...")
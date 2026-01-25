# Checking that a number that user enter is armstrong or not

no = int(input("Enter the No : ")) # 153

# digit = 3
digit = len(str(no)) # 153 = len-> 3

# in the for loop if we don't give start iteration so automatically it will considering and taking as 0
# so here i goes 0 to digit means for 153 numbers 0 to 3 means i = 0 , 1 , 2

sum = 0
temp = no

for i in range(digit) : 
    rem = no % 10
    sum = sum + pow(rem , digit) # sum += pow(rem , digit)
    no = no//10

if sum == temp :
    print(temp,"is an Armstrong No...")
else :
    print(temp,'is not an Armstrong No...')
    
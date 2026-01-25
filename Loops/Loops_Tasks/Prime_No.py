# checking that users enters a numbers is prime or not

# Method No - 1 :-

no = int(input('Enter the No : '))

count = 0

for i in range(1 , no + 1) :
    if no % i == 0 :
        count += 1 # count = count + 1 -- Assignment Opeartions

if count == 2 :
    print(no,'is a Prime No...')
else :
    print(no,"is not a Prime No...")

# ---------------------------------------------------------------------------------

# Method No - 2 :-

# no = int(input("Enter the No : "))

# for i in range(2 , no) :
#     if (no % i) == 0 :
#         print(no,'is not a Prime No...')
#         break
# else :
#     print(no,"is a Prime No...")
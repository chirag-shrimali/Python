# write the python program to check the greatest of 3 numbers entered by the user

no1 = int(input("\nEnter the No1 : "))

no2 = int(input("\nEnter the No2 : "))

no3 = int(input("\nEnter the No3 : "))

# if(no1 >= no2 and no1 >= no3) :
#     print("\nNo1 is Greater...")
# elif no2 > no3 :
#     print("\nNo2 is Greater...")
# else :
#     print("\nNo3 is Greater...")

if(no1 > no2 and no1 > no3) :
    print("\nNo1 is Greatest...")
elif no2 > no1 and no2 > no3 :
    print("\nNo2 is Greatest...")
else :
    print("\nNo3 is Greatest...")
# finding the range of palindrome number and number that users enters

# no = int(input("Enter the No : "))
start = int(input("Enter the Starting Number : "))
end = int(input('Enter the Ending Number : '))

# rev = 0
# dup = no
# digit = len(str(no))


for i in range(start , end + 1) :
    rev = 0
    digit = len(str(i))
    dup = i
    for j in range(digit) :
        rem = dup % 10
        rev = (rev * 10) + rem
        dup = dup//10 # dup //= 10

    if rev == i :
        print(i,end=" ")
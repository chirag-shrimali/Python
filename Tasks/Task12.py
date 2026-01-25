# Finding the greatest numbers of the four numbers that users enters

a = int(input("Enter the No1 : "))
b = int(input("Enter the No2 : "))
c = int(input("Enter the No3 : "))
d = int(input("Enter the No4 : "))

if(a > b and a > c and a > d) :
    print('A is Greatest Numbers among this three...')

elif(b > a and b > c and b > d) :
    print("B is Greatest Numbers among this three...")

elif(c > a and c > b and c > d) :
    print("C is Greatest Numbers among this three...")

else :
    print("D is Greatest Numbers among this three...")
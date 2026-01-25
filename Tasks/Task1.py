# Take the three integer inputs from users

a = int(input("Enter the No1 : "))
b = int(input("Enter the No2 : "))
c = int(input("Enter the No3 : "))

if a > b and a > c and b > c :
    print("A is Larger , B is Medium , C is Smaller")
elif a > b and a > c and c > b :
    print("A is Larger , C is Medium , B is Smaller")
elif b > a and b > c and a > c :
    print("B is Larger , A is Medium , C is Smaller")
elif b > a and b > c and c > a :
    print("B is Larger , C is Medium , A is Smaller")
elif c > a and c > b and a > b :
    print("C is Larger , A is Medium , B is Smaller")
elif c > a and c > b and b > a :
    print("C is Larger , B is Medium , A is Smaller")
# elif a > c and c > b :
#     print("A is Larger , C is Medium , B is Smaller")
# elif c > a & a > b :
#     print("C is Larger , A is Medium , B is Smaller")
# elif c > b and b > a :
#     print("C is Larger , B is Medium , A is Smaller")
# elif a > b and a > c and b == c :
#     print("A is Big , B and C Equals")
# elif b > a and b > c and a == c :
#     print("B is Big , A and C Equals")
# elif c > b and c > a & a == b :
#     print("C is Big , A and B Equals")
# elif a == b == c :
#     print("A , B , C Equals")
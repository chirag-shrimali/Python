"""
Ask user to give name and marks of 5 different students. Store them in dictionary. 
and sorted by marks 
ram 90 sita 77  ravan 66 
output  :{"ram":90,"sita":77,"ravan":66}

sorted by marks  :
output  : {"ravan" :66, "sita" : 77,"ram" :90}
"""

n1 = input("Enter the First Student Name : ")
m1 = int(input("Enter the Marks of Student - 1 : "))
print('------------------------------------------------------')
n2 = input("Enter the Second Student Name : ")
m2 = int(input("Enter the Marks of Student - 2 : "))
print('------------------------------------------------------')
n3 = input("Enter the Third Student Name : ")
m3 = int(input("Enter the Marks of Student - 3 : "))
print('------------------------------------------------------')
n4 = input("Enter the Fourth Student Name : ")
m4 = int(input("Enter the Marks of Student - 4 : "))
print('------------------------------------------------------')
n5 = input("Enter the Fifth Student Name : ")
m5 = int(input("Enter the Marks of Student - 5 : "))
print('------------------------------------------------------')

d1 = {}

d1.setdefault(n1 , m1)
d1.setdefault(n2 , m2)
d1.setdefault(n3 , m3)
d1.setdefault(n4 , m4)
d1.setdefault(n5 , m5)

print(d1)

v = d1.values()

sort = sorted(v)

d1.setdefault(n1 , m1)
d1.setdefault(n2 , m2)
d1.setdefault(n3 , m3)
d1.setdefault(n4 , m4)
d1.setdefault(n5 , m5)

print(sort)
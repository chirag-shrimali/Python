'''

ecom :

users.txt

stock.txt

id  name    price  qty
1   iPhone  2000   200

enter product name :

iPhone -> it is available price is 2000 -->
please enter 1 for purchase...

please enter your full name :
Chirag Shrimali : if avialble welcome back if not add it in file and welcome to app...

order.txt
name             product   price
Chirag Shrimali  iPhone    2000  

stock should decrease...

'''

# file = open('order.txt' , "w")

# file.write(f"NAME \t\t PRODUCT \t PRICE \t")

# file.close()

names = ['Chirag Shrimali' , 'Suresh Patel' , 'Rajesh Mehta' , 'Paresh Shah' , 'Ketan Pandit' , 'Hamza Ali Mazri' , 'Rehman Dakait' , 'Babu Dakait' , 'Ujair Balaoch']

users = {1 : ["IPhone" , 2000 , 200] , 2 : ['Vivo' , 5000 , 100] , 3 : ['Samsung' , 7000 , 50] , 4 : ['RealMe' , 4000 , 25] , 5 : ['Galaxy' , 6000 , 36]}

file = open('stock.txt' , "w")

file.write(f"ID \t\t  NAME \t\t  PRICE \t\t  QUANTITY \n")

for i , j in users.items() :

    if len(j[0]) < 7 :

        file.write(f"{i}\t\t {j[0]}\t\t {j[1]}\t\t\t {j[2]}\n")

    else :

        file.write(f"{i}\t\t {j[0]}\t {j[1]}\t\t\t {j[2]}\n")

product_name = input("Enter the Product Name : ").capitalize()

if product_name in "stock.txt" :

    # pur = int(input("Please , Enter 1 for Purchase : "))

    for i in names :

        file1 = open('order.txt' , "w")

        fullName = input("Please , Enter Your Full Name : ")

        file1.write(f"NAME \t\tPRODUCT \tPRICE")

        print(f"{fullName} \t\t {j[0]} \t{j[1]}")

file.close()


# for i in users :

#     if fullName in users :

#         print(f'Welcome Back , {fullName} !!')

#         break

#     else :

#         users.append(i)

#         break
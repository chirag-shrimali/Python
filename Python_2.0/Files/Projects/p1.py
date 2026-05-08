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

# ---------------- E-COMMERCE SYSTEM ----------------

# Author : Chirag Shrimali

# Files Used :
# users.txt
# stock.txt
# order.txt

# ---------------- STOCK DATA ----------------

# -------------------------------------------------
# E-COMMERCE MANAGEMENT SYSTEM
# Author : Chirag Shrimali
# -------------------------------------------------

import os

# -------------------------------------------------
# CREATE FILES IF NOT EXISTS
# -------------------------------------------------

if not os.path.exists("users.txt"):
    open("users.txt", "w").close()

if not os.path.exists("order.txt"):
    open("order.txt", "w").close()

# Create stock file only first time
if not os.path.exists("stock.txt"):

    stockFile = open("stock.txt", "w")

    stockFile.write("ID\tNAME\t\tPRICE\tQUANTITY\n")
    stockFile.write("1\tiPhone\t\t2000\t200\n")
    stockFile.write("2\tVivo\t\t5000\t100\n")
    stockFile.write("3\tSamsung\t\t7000\t50\n")
    stockFile.write("4\tRealMe\t\t4000\t25\n")
    stockFile.write("5\tGalaxy\t\t6000\t36\n")

    stockFile.close()

# -------------------------------------------------
# READ STOCK FILE
# -------------------------------------------------

products = {}

stockFile = open("stock.txt", "r")

lines = stockFile.readlines()

stockFile.close()

for line in lines[1:]:

    parts = line.split()

    # Skip Empty Lines
    if len(parts) == 0:
        continue

    pid = int(parts[0])
    name = parts[1]
    price = int(parts[2])
    qty = int(parts[3])

    products[pid] = [name, price, qty]

# -------------------------------------------------
# DISPLAY PRODUCTS
# -------------------------------------------------

print("\n----------- AVAILABLE PRODUCTS -----------\n")

print("ID\tNAME\t\tPRICE\tQUANTITY")

for pid, data in products.items():

    name = data[0]
    price = data[1]
    qty = data[2]

    if len(name) < 8:
        print(f"{pid}\t{name}\t\t{price}\t{qty}")
    else:
        print(f"{pid}\t{name}\t{price}\t{qty}")

# -------------------------------------------------
# SEARCH PRODUCT
# -------------------------------------------------

productName = input("\nEnter Product Name : ").capitalize()

found = False

for pid, data in products.items():

    name = data[0]
    price = data[1]
    qty = data[2]

    if productName == name:

        found = True

        print(f"\n{name} is Available")
        print(f"Price : {price}")
        print(f"Quantity : {qty}")

        # Check Stock
        if qty <= 0:
            print("\nProduct Out Of Stock")
            break

        purchase = int(input("\nEnter 1 For Purchase : "))

        if purchase == 1:

            # -------------------------------------------------
            # USER LOGIN / REGISTER
            # -------------------------------------------------

            fullName = input("\nEnter Your Full Name : ")

            usersFile = open("users.txt", "a+")

            usersFile.seek(0)

            users = usersFile.read().splitlines()

            if fullName in users:

                print(f"\nWelcome Back {fullName} !!")

            else:

                usersFile.write(fullName + "\n")

                print(f"\nWelcome To E-Commerce App {fullName} !!")

            usersFile.close()

            # -------------------------------------------------
            # SAVE ORDER
            # -------------------------------------------------

            orderFile = open("order.txt", "a")

            orderFile.write(f"{fullName}\t{name}\t{price}\n")

            orderFile.close()

            # -------------------------------------------------
            # UPDATE STOCK
            # -------------------------------------------------

            products[pid][2] -= 1

            print("\nOrder Placed Successfully !!")

            print(f"Remaining Quantity : {products[pid][2]}")

            # -------------------------------------------------
            # SAVE UPDATED STOCK
            # -------------------------------------------------

            stockFile = open("stock.txt", "w")

            stockFile.write("ID\tNAME\t\tPRICE\tQUANTITY\n")

            for sid, sdata in products.items():

                sname = sdata[0]
                sprice = sdata[1]
                sqty = sdata[2]

                if len(sname) < 8:
                    stockFile.write(f"{sid}\t{sname}\t\t{sprice}\t{sqty}\n")
                else:
                    stockFile.write(f"{sid}\t{sname}\t{sprice}\t{sqty}\n")

            stockFile.close()

        else:

            print("\nPurchase Cancelled")

        break

# -------------------------------------------------
# PRODUCT NOT FOUND
# -------------------------------------------------

if found == False:

    print("\nProduct Not Found")

# -------------------------------------------------
# SHOW UPDATED STOCK
# -------------------------------------------------

print("\n----------- UPDATED STOCK -----------\n")

updatedStock = open("stock.txt", "r")

print(updatedStock.read())

updatedStock.close()
print('\n\t\t\t-------Welcome to Royal Hotel-------')

print('\n+-----Here are the Choices of our hotel-----+')
print('|\t\t1.Punjabi Dish              |')
print('|\t2.Kathyawadi Dish                   |')
print('|\t\t3.South Indian              |')
print('|\t4.Chinese Dish                      |')
print('+-------------------------------------------+')

choice = int(input("Enter Your Choice (1-4) : "))

match choice :
    case 1 : 
            print('Which Items that you want to order in Punjabi_Dish.\n\n'
                  '1. Paneer Ki Sabji - Rs.150/-'
                  '\n2. Chole Bhature - Rs.180/-'
                  '\n3. Butter Milk - Rs.30/-'
                  '\n4. Naan Roti - Rs.35/-')
            ch = int(input("\nEnter Your Choice According to the Menu : "))
            quantity = int(input("Enter Your Quantity : "))
            
            if ch == 1 : 
                price = 150 
                item = "Paneer Ki Sabji"
            elif ch == 2 :
                 price = 180
                 item = "Chole Bhature"
            elif ch == 3 :
                  price = 30
                  item = "Butter Milk"
            elif ch == 4 :
                  price = 35
                  item = "Naan Roti"
            else :
                  print("Invalid Choice!!!")
                  exit()

            total = quantity * price
            print('You are Ordering' , item , 'So,Your Total Bill is :',total)
            print('*****Thanks for visiting Royal Hotel*****')

    case 2 : 
            print('Which Items that you want to order in Kathyawadi_Dish.\n\n'
                  '1. Sev Tameta Ki Sabji - Rs.130/-'
                  '\n2. Kaddi Khichdi - Rs.90/-'
                  '\n3. Bajre Ka Rotla - Rs.25/-'
                  '\n4. Butter Milk - Rs.25/-')
            ch = int(input("\nEnter Your Choice According to the Menu : "))
            quantity = int(input("Enter Your Quantity : "))
            
            if ch == 1 : 
                price = 130 
                item = "Sev Tameta Ki Sabji"
            elif ch == 2 :
                 price = 90
                 item = "Kaddi Khichdi"
            elif ch == 3 :
                  price = 25
                  item = "Bajre Ka Rotla"
            elif ch == 4 :
                  price = 25
                  item = "Butter Milk"
            else :
                  print("Invalid Choice!!!")
                  exit()

            total = quantity * price
            print('You are Ordering' , item , 'So,Your Total Bill is :',total)
            print('*****Thanks for visiting Royal Hotel*****')

    case 3 : 
            print('Which Items that you want to order in South_Indian.\n\n'
                  '1. Masala Dosa - Rs.40/-'
                  '\n2. Idli - Rs.30/-'
                  '\n3. Sambhar & Chutney - Rs.20/-'
                  '\n4. Kantha Vada - Rs.25/-')
            ch = int(input("\nEnter Your Choice According to the Menu : "))
            quantity = int(input("Enter Your Quantity : "))
            
            if ch == 1 : 
                price = 40 
                item = "Masala Dosa"
            elif ch == 2 :
                 price = 30
                 item = "Idli"
            elif ch == 3 :
                  price = 20
                  item = "Sambhar & Chutney"
            elif ch == 4 :
                  price = 25
                  item = "Kantha Vada"
            else :
                  print("Invalid Choice!!!")
                  exit()

            total = quantity * price
            print('You are Ordering' , item , 'So,Your Total Bill is :',total)
            print('*****Thanks for visiting Royal Hotel*****')

    case 4 : 
            print('Which Items that you want to order in Chinese_Dish.\n\n'
                  '1. Manchuriyan - Rs.70/-'
                  '\n2. Soup - Rs.85/-'
                  '\n3. Paneer Chili - Rs.110/-'
                  '\n4. Noodles - Rs.95/-')
            ch = int(input("\nEnter Your Choice According to the Menu : "))
            quantity = int(input("Enter Your Quantity : "))
            
            if ch == 1 : 
                price = 70 
                item = "Manchuriyan"
            elif ch == 2 :
                 price = 85
                 item = "Soup"
            elif ch == 3 :
                  price = 110
                  item = "Paneer Chili"
            elif ch == 4 :
                  price = 95
                  item = "Noodles"
            else :
                  print("Invalid Choice!!!")
                  exit()

            total = quantity * price
            print('You are Ordering' , item , 'So,Your Total Bill is :',total)
            print('*****Thanks for visiting Royal Hotel*****')
# Write the Python Program to calculate the rent

"""  
Input from the user :

Total Rent
Total Food Ordered for snacking
Electricity units spend
Charge per unit
Persons living in room / flat

Output :-

Total amount you have to pay is...
"""

import os
os.system('cls' if os.name == 'nt' else 'clear')

def show_rent_intro():
    print(r"""
██████╗ ███████╗███╗   ██╗████████╗     ██████╗ █████╗ ██╗      ██████╗
██╔══██╗██╔════╝████╗  ██║╚══██╔══╝    ██╔════╝██╔══██╗██║     ██╔════╝
██████╔╝█████╗  ██╔██╗ ██║   ██║       ██║     ███████║██║     ██║     
██╔══██╗██╔══╝  ██║╚██╗██║   ██║       ██║     ██╔══██║██║     ██║     
██║  ██║███████╗██║ ╚████║   ██║       ╚██████╗██║  ██║███████╗╚██████╗
╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝        ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝

                M O N T H L Y   E X P E N S E   S P L I T T E R
    """)
    print("=" * 70)
    print("              Calculate Smart. Split Fair. Live Easy.")
    print("=" * 70 + "\n")

show_rent_intro()

#         Type - Casting
#              |
total_rent = int(input("\nEnter the Total Rent For Hostel Room / Flat : "))

total_food_ordered = int(input("\nEnter the Total Food Ordered For Snacking : "))

electricity_unit_spent = int(input("\nEnter the Electricity Units that you spent for : "))

charge_per_unit = int(input("\nEnter the Charge Per Units : "))

person = int(input("\nEnter the Persons that are living in the Room / Flat : "))

total_bill = electricity_unit_spent * charge_per_unit

final_bill = (total_rent + total_food_ordered + total_bill) // person

print("\nThe Total Amount that you have to pay is :",final_bill)
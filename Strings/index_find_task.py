# task : 1 

"""
input : "i am going to goa next month." 
output : 1 st o index number : 6
         2 nd o index number : 12
         3 rd o index number : 15
         4 th o index number : 24
"""

input = "I am going to goa next month."

length = len(input)

count = 1

for i in range(length) :    
        print(f"\nThe {count} O index number is :",input.find("o" , i))
        count += 1
    # break

# print("\nThe First O index number is :",input.find("o"))
# print("\nThe Second O index number is :",input.find("o",7))
# print("\nThe Third O index number is :",input.find("o",13))
# print("\nThe Fourth O index number is :",input.find("o",16))
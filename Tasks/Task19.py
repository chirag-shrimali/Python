# Calculate the Birthdate/month

birth_date = int(input("Enter Your Birth_Date : "))

birth_date_month = int(input("Enter Your Birth_Date_Month : "))

final = (((((birth_date * 2) + 5) * 50) + birth_date_month) - 250)

# add = mul + 5

# mul1 = add * 50

# add1 = mul + 11 # add month of your birthday

# sub = add1 - 250

print("Your Birthday is :",final)
# give 20 % discount if unit is above 200 else 10% discount give after discount list
# ["171","90",160]....

# units = [190 , 100 , 200 , 300 , 334 , 70 , 50 , 400 , 450 , 10 , 110]

# units = [190 , 100 , 200 , 300 , 334 , 70 , 50 , 400 , 450 , 10 , 110]

# units1 = []

# for i in units :
#     if i > 200 :
#         i = i // 1.2
#     else :
#          i = i // 1.1

#     units1.append(i)

# print(units1)

# Comprehension Version

units = [190 , 100 , 200 , 300 , 334 , 70 , 50 , 400 , 450 , 10 , 110]

units1 = [i // 1.2 if i > 200 else i // 1.1 for i in units]

print(units1)
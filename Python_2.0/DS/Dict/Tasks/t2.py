data = {"Virat" : [122 , 150 , 60] , "Rohit" : [45 , 140 , 188]}

# print(data)

# sum = 0

# for i , j in data.items() :
#     # print(f"{j}")
#     for run in j :
#         sum += run
#         print(run)

# print("\nThe Total Sum of the Score of both players are :",sum)

# sum = 0

# for i , j in data.items() :
#     # print(f"{j}")
#     for run in j :
#         sum += run
#         print(run)

#     print("----",sum)
#     sum = 0

# Maximum Score Finding ---------------------------------

max = 0

for i in data.values() :
    for run in i :
        if run > max :    
            max = run

print(f"\nHighest Score is :",max)
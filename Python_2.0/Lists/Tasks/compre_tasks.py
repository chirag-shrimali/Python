# give 20 % discount if unit us above 200 else 10% disaocunt give  after discount list
# ["171","90",160]....

# units=[190 , 100 , 200 , 300 , 334 , 70 , 50 , 400 , 450 , 10 , 110]

# -------------------------------------------------------------------------------------------

# print both player name
# print virat score 
# Print virat score total
# print rohit score total
# print total score by both player

# players =[
#     ["Virat" , 100 , 121 , 89] ,
#     ["Rohit" , 100 , 67 , 56]
#     ]

# # 1

# players1 = []

# for i in range(0 , len(players)) :
#     players1.append(i)
    
# print(players[0][0])
# print(players[1][0])

# 2

# players1 = []

# for i in range(0 , len(players)) :
#     players1.append(i)
    
# print(players[0][1] , players[0][2] , players[0][3])

# 3 

# players1 = []

# for i in range(0 , len(players)) :
#     players1.append(i)
    
# print("Virat Total Scores :",players[0][1] + players[0][2] + players[0][3])
# print("Rohit Total Scores :",players[1][1] + players[1][2] + players[1][3])

# 4

# players1 = []

# for i in range(0 , len(players)) :
#     players1.append(i)
    
# print(players[0][1] , players[0][2] , players[0][3])
# print(players[1][1] , players[1][2] , players[1][3])

# ----------------------------------------------------------------------------------

players =[
    ["Virat" , 100 , 121 , 89] ,
    ["Rohit" , 100 , 67 , 56]
    ]

# 1

# players1 = []

# for i in range(0 , len(players)) :
#     for j in range(0 , len(players[i])) :
#         player = players[i][0]
#         players1.append(player)
#         break

# print(players1)

# 2

players1 = []

for i in range(0 , len(players)) :
    for j in range(0 , len(players[i])) :
        player = players[i][1] , players[i][2] , players[i][2]
        players1.append(player)
        break

# print(players1)

# 3

# players1 = []

# for i in range(0 , len(players)) :
#     # for j in range(0 , len(players[i])) :
#         player = players[i][1] + players[i][2] + players[i][2]
#         players1.append(player)
#         break

# print("Virat Scores are :",players1)

# 4

# players1 = []

# for i in range(1 , len(players)) :
#     # for j in range(0 , len(players[i])) :
#         player = players[i][1] + players[i][2] + players[i][2]
#         players1.append(player)
#         break

# print("Rohit Scores are :",players1)

# 5

players1 = []

for i in range(0 , len(players)) :
    for j in range(0 , len(players[i])) :
        player = players[i][1] , players[i][2] , players[i][2]
        players1.append(player)
        break
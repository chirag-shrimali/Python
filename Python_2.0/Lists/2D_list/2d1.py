# in the python the inner nested list is known as 2D List

# Fruits = ['Lamon' , 'Chiku' , "Watermelon" , "Orange"]

# Foods = ['Chinese' , 'Punjabi' , "Gujarati" , "South Indian"]

# Languages = ['C' , 'C++' , "Python" , "Java"]

# #          0        1        2

# Items = [Fruits , Foods , Languages]

# # print(Items) # print whole lists items as Lists

# # print(Items[0]) # print the index 0's Fruits inside elements as Lists

# # print(Items[1]) # Foods Lists Print

# # print(Items[2]) # Languages Lists Print

# print(Items[0][0]) # elements print Lamon

# print(Items[0][1]) # elements print Chiku

# print(Items[0][2]) # elements print Watermelon

# print(Items[0][3]) # elements print Orange

# print(Items[1][0]) # elements print Chinese

# print(Items[1][1]) # elements print Punjabi

# print(Items[1][2]) # elements print Gujarati

# print(Items[1][3]) # elements print South Indian

# print(Items[2][0]) # elements print C

# print(Items[2][1]) # elements print C++

# print(Items[2][2]) # elements print Python

# print(Items[2][3]) # elements print Java

# print(Items[3][0]) # error shows that lists index out of the range

# ----------------------------------------------------------------------------

#               0         1          2             3

# Items = [   ['Lamon' , 'Chiku' , "Watermelon" , "Orange"] , # 0 
# #               0           1            2             3 
#             ['Chinese' , 'Punjabi' , "Gujarati" , "South Indian"] , # 1 
# #             0      1        2          3   
#             ['C' , 'C++' , "Python" , "Java"] # 2
#          ]

# for i in Items :
#     print(i)

# for i in Items :
#     for j in i :
#         print(j)

# for i in Items :
#     for j in i :
#         print(j , end = " ")
#     print()

# ----------------------------------------------------------------------------------------------

# Digits = [ [1 , 2 , 3] ,
#            [4 , 5 , 6] ,
#            [7 , 8 , 9] ,
#            ['*' , 0 , '#'] ,
#            [' ' , '📞' , ' ']
#          ]

# for i in Digits :
#     print(i)

# for i in Digits :
#     for j in i :
#         print(j)
    
# for i in Digits :
#     for j in i :
#         print(j , end = "  ")
#     print()

# -------------------------------------------------------------------------------------------------------

# print both player name
# print virat score 
# Print virat score total
# print rohit score total
# print total score by both player

players = [
#               0       1     2    3
            ["Virat" , 100 , 121 , 89] ,
#               0       1     2    3
            ["Rohit" , 100 , 67 , 56]
          ]

# 1

# for i in range (0 , len(players)) :
#     for j in range(0 , len(players[i])) :
#         player = players[i][0] 
#         print(player , end = " ")
#         break
#     print()

# 2

# for i in range (0 , len(players) - 1) :
#     for j in range(0 , len(players[i]) - 1) :
#         player = players[i][1] , players[i][2] , players[i][3] 
#         print(player , end = " ")
#         break
#     print()

# 2(a)

# for i in range (1 , len(players)) :
#     for j in range(1 , len(players[i])) :
#         player = players[i][1] , players[i][2] , players[i][3] 
#         print(player , end = " ")
#         break
#     print()

# 3

# for i in range (0 , len(players) - 1) :
#     for j in range(0 , len(players[i]) - 1) :
#         player = players[i][1] + players[i][2] + players[i][3] 
#         print(player , end = " ")
#         break
#     print()

# 4

# for i in range (1 , len(players)) :
#     for j in range(1 , len(players[i])) :
#         player = players[i][1] + players[i][2] + players[i][3] 
#         print(player , end = " ")
#         break
#     print()

# 5

for i in range (0 , len(players)) :
    for j in range(0 , len(players[i])) :
        player = players[i][1] , players[i][2] , players[i][3]  
        print(player , end = " ")
        break
    print()
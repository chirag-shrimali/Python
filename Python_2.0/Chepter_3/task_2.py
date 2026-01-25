# Write a Program that takes your favorite food name as input and prints :-

"""
1. The Middle 3 Characters
2. The Last 2 Characters
"""

fav_food = input("\nEnter Your Favorite Food Name : ")

mid_part = len(fav_food) // 2

last_output = fav_food[mid_part - 1 : mid_part + 2]

print(last_output)

print(fav_food[-2:])
# Write a python program that takes any word or sentence as input and prints :-

"""
1. The First Character
2. The Last Character
3. The Total number of characters
"""

sentence = input("\nEnter the Sentence : ")

first_ch = sentence[0]

last_ch = sentence[-1]

total_ch = len(sentence)

print("\nThe First Character is :",first_ch)

print("\nThe Last Character is :",last_ch)

print("\nThe Total numbers of Character are :",total_ch)
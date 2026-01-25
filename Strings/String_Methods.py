# There are having so many different - different types of methods in the string like checking conditions , join , replace , find , upper , lower and so on

# ---------------------------------------------------------------------------

# 1. Slicing the string --> string[start_index , end_index] --> start_index included where end_index excluded

# string = 'Chirag'

# print(string[0:6]) # print string in the index of 0 to 5 means here Chirag
# print(string[2:5]) # between 2 to 4 means ira prints
# print(string[5:6]) # between 5 and 5 means g only

# print(string[:]) # means the string always starts with 0 and go to upto their length means here length is 6 so 0:6 means between 0 to 5 means prints Chirag
# print(string[0:]) # prints 0 to length so prints Chirag similar to 0 to 6
# print(string[:6]) # starts always 0 so between 0 to 5 means Chirag similar to 0 to 6

# print(string[-5:-2]) # similar to [1:4] means prints between 1 to 3 string so here prints hir whenever negative slicing given first of all converts it is in positive so simplify it is
# print(string[-3:-1]) # [3:5] means between 3 to 4 string prints so here prints ra

# print(string[-5:-2] + string[-3:-1])

# string = "Mathematics"

# print(string[0:8:2])  # between Mathemat --> Mtea

# print(string[-9:-1:3]) # between thematic --> tmi

# ---------------------------------------------------------------------------

# 2. len of string

# string = 'Chirag'

# print(string) # Chirag
# print(len(string)) # 6

# ---------------------------------------------------------------------------

# 3. count the str or particular character in the string that how many times that repeats

# string = 'Chirag Shrimali'

# print(string) # Chirag Shrimali
# print(string.count('i')) # 3
# print(string.count('r')) # 2
# print(string.count('')) # 16
# print(string.count(' ')) # 1
# print(string.count('c')) # 0

# ---------------------------------------------------------------------------

# 4. finding a str or chr in the string that which index value are there

# string = "Chirag"

# print(string) # Chirag
# print(string.find('r')) # 3
# print(string.find('')) # 0
# print(string.find(" ")) # -1
# print(string.find('c')) # -1

# ---------------------------------------------------------------------------

# 5. Capitalize , Lower , Upper

# string = 'chIrAg'

# print(string)
# print("--------------------")

# cap_str = string.capitalize()
# print("Capitalize :",cap_str)

# lo_str = string.lower()
# print("Lower :",lo_str)

# up_str = string.upper()
# print("Upper :",up_str)

# ---------------------------------------------------------------------------

# 6. Replace the existing string with another string which can be enters by the users

# string = "Chirag is a nice boy.He is a excellent Personality too."

# print(string) # Chirag is a nice boy.He is a excellent Personality too.
# print(string.replace('excellent' , "good").replace('nice' , "excellent"))

# ----------------------------------------------------------------------------
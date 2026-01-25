# String are Immutable...

# String Methods :-

'''
C - 0
h - 1
i - 2
r - 3
a - 4
g - 5
'''

"""
S - 0
h - 1
r - 2
i - 3
m - 4
a - 5
l - 6
i - 7
"""

# name = "Chirag"

# name1 = "Shrimali"

# # Concatenations----------------------------------------------------------------

# name = "Chirag"

# name1 = "Shrimali"

# print(name + " " + name1) # Chirag Shrimali

# # Length------------------------------------------------------------------------

# name = "Chirag"

# name1 = "Shrimali"

# print(len(name)) # 6

# print(len(name1)) # 8

# print(len(name + " " + name1)) # 15

# # Index Value-------------------------------------------------------------------

# # name = "Chirag"

# name1 = "Shrimali"

# print(name1[0]) # S

# print(name1[3]) # i

# print(name1[6]) # l

# print(name1[5]) # a

# # print(name1[9]) # string index out of the range(interval)

# # Slicing-----------------------------------------------------------------------

# name = 'Chirag'

# """
# C -> -6
# h -> -5
# i -> -4
# r -> -3
# a -> -2
# g -> -1
# """

# print(name[0:4]) # Chir

# print(name[:4]) # Chir

# print(name[0:]) # Chirag

# print(name[0:5]) # Chira

# print(name[2:5]) # ira

# print(name[1:4]) # hir

# print(name[-5:-1]) # hira

# print(name[-5:]) # hirag

# # UpperCase-------------------------------------------------------

# str = "ChIrAg"

# print(str.upper()) # CHIRAG

# # LowerCase-------------------------------------------------------

# str = "ChIRAg"

# print(str.lower()) # chirag

# # Count-----------------------------------------------------------

# str = "Chirag Shrimali"

# print(str.count('i')) # 3

# # Capitalize--------------------------------------------------------

# str = "cHiRag shRiMAlI"

# print(str.capitalize()) # Chirag shrimali

# # Title--------------------------------------------------------------

# str = 'chIrAg shRiMAli'

# print(str.title()) # Chirag Shrimali

# # EndsWith & StartsWith------------------------------------------------

# str = "Chirag"

# print(str.startswith('C')) # True

# print(str.startswith("hi")) # False

# print(str.startswith('Chi')) # True

# print(str.endswith("g")) # True

# print(str.endswith("ra")) # False

# print(str.endswith('rag')) # True

# # Find--------------------------------------------------------------------

# str = "Chirag Shrimali"

# print(str.find('i')) # 2

# print(str.find("C")) # 0

# print(str.find('ag')) # 4

# print(str.find("i" , 3)) # 10

# print(str.find('r' , 4)) # 9

# # rFind---------------------------------------------------------------------

# str = 'Chirag Shrimali'

# print(str.rfind('i')) # 14

# print(str.rfind("C")) # 0

# print(str.rfind('ag')) # 4

# print(str.rfind("i" , 5)) # 14

# print(str.rfind('r' , 9)) # 9

# print(str.rfind('r' , 10)) # -1

# # Index--------------------------------------------------------------------

# str = "Chirag Shrimali"

# print(str.index('i')) # 2

# print(str.index("C")) # 0

# print(str.index('ag')) # 4

# print(str.index("i" , 3)) # 10

# print(str.index('r' , 4)) # 9

# # rIndex---------------------------------------------------------------------

# str = 'Chirag Shrimali'

# print(str.rindex('i')) # 14

# print(str.rindex("C")) # 0

# print(str.rindex('ag')) # 4

# print(str.rindex("i" , 5)) # 14

# print(str.rindex('r' , 9)) # 9

# # print(str.rindex('r' , 10)) # -1

# # Replace-----------------------------------------------------

# str = "Chirag Shrimali"

# print(str.replace(" " , "_")) # Chirag_Shrimali

# print(str.replace("i" , 'a')) # Charag Shramala

# # Split & rsplit-----------------------------------------------------------

# str = "Chirag Shrimali is a Nice Person."

# print(str.split()) # ['Chirag' , 'Shrimali' , 'is' , 'a' , 'Nice' , 'Person.']

# print(str.split("i")) # ['Ch' , 'rag Shr' , 'mal' , ' ' , 's a N' , 'ce Person.']

# print(str.split('a')) # ['Chir' , 'g Shrim' , 'li is ' , ' Nice Person.'] 

# print(str.rsplit()) # ['Chirag' , 'Shrimali' , 'is' , 'a' , 'Nice' , 'Person.']

# print(str.rsplit("i")) # ['Ch' , 'rag Shr' , 'mal' , ' ' , 's a N' , 'ce Person.']

# print(str.rsplit('a')) # ['Chir' , 'g Shrim' , 'li is ' , ' Nice Person.']

# # partition--------------------------------------------------------------------

# str = 'Chirag Shrimali is a Nice Person.'

# print(str.partition('i')) # ('Ch' , 'i' , 'rag Shrimali is a Nice Person.')

# print(str.partition('a')) # ('Chir' , 'a' , 'g Shrimali is a Nice Person.')

# print(str.partition('li')) # ('Chirag Shrima' , 'li' , ' is a Nice Person.')

# print(str.rpartition('i')) # ('Chirag Shrimali is a N' , 'i' , 'ce Person.')

# print(str.rpartition('a')) # ('Chirag Shrimali is ' , 'a' , ' Nice Person.')

# print(str.rpartition('li')) # ('Chirag Shrima' , 'li' , ' is a Nice Person.')

# # Membership----------------------------------------------------------------------

# str = "Chirag"

# print('i' in str) # True

# print('l' in str) # False

# print('ra' in str) # True

# # Repetition-------------------------------------------------------------------------

# str = "Chirag "

# print(str * 3) # Chirag Chirag Chirag
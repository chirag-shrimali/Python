# string is a data type of the python which can be used for storing sequence of the characters

# concat--------------------------------------------------------------------------------------

# '+' operators

# str1 = "Chirag"

# str2 = 'Shrimali'

# final_str = str1 + " " + str2

# print(final_str)

# length--------------------------------------------------------------------------------------

# len() function

# str1 = 'Chirag'

# str2 = "Shrimali"

# final_str = str1 + " " + str2

# len1 = len(str1)

# len2 = len(str2)

# len3 = len(final_str)

# print("\nThe Length of first string are :",len1) # 6

# print('\nThe Length of second string are :',len2) # 8

# print("\nThe Final String length are :",len3) # 14

# indexing --------------------------------------------------------------------------

# position of the string

# str1 = "Chirag Shrimali"

# print(str1) # Chirag Shrimali

# print(str1[0]) # C

# print(str1[1]) # h

# print(str1[4]) # a

# print(str1[8]) # h

# print(str1[10]) # i

# print(str1[14]) # i

# print(str1[15]) # IndexError : string index out of the range.

# str[0] = "c"

# print(str) # TypeError : Object item assignment does not support.

# Positive Slicing -------------------------------------------------------------------------

# [starting_index : ending_index : step_size] ---> starting_index including where ending_index excluding

# str = "Chirag Shrimali"

# print(str) # Chirag Shrimali

# print(str[1 : 4]) # hir

# print(str[ : 5]) # Chira  --> starts with 0 and goes upto 0 to 5

# print(str[3 : ]) # rag Shrimali --> goes upto 3 to len(str)

# print(str[ : ]) # Chirag Shrimali --> starts with 0 and goes 0 to len(str)

# print(str[ : : -1]) # ilamirhS garihC --> it will converts the string into reverse

# Negative Slicing -------------------------------------------------------------------------

# str = 'Chirag Shrimali'

# print(str) # Chirag Shrimali

# print(str[-2]) # l

# print(str[-5]) # i
 
# print(str[-14]) # h

# print(str[-15]) # C

# print(str[-8]) # S

# print(str[-6 : -1]) # rimal

# print(str[-12 : -4 : 2]) # rgSr

# print(str[-16]) # IndexError : string index out of the range

# functions :-

# endswith() & startswith() ----------------------------------------------------------------

# str = 'Chirag Shrimali'

# print(str) # Chirag Shrimali

# print(str.startswith("Chr")) # False

# print(str.startswith('Ch')) # True

# print(str.endswith("li")) # True

# print(str.endswith('il')) # False

# Capitalize() & Title() ------------------------------------------------------------------------------

# Capitalize() ---> convert the string first character only capital

# Title() ---> convert the string first character capital after every white space

# str = 'cHiRaG sHriMalI gIrISh kUmar'

# print(str) # cHiRaG sHriMalI gIrISh kUmar

# print(str.capitalize()) # Chirag shrimali girish kumar

# print(str.title()) # Chirag Shrimali Girish Kumar

# Replace() ------------------------------------------------------------------------------------------

# Replace(odd_str , new_formatted_str)

# str = "Chirag Shrimali"

# print(str) # Chirag

# print(str.replace("i" , 'a').replace(' ' , "_")) # Charag_Shramala

# Find() --------------------------------------------------------------------------------------------

# Find() ---> which can be find out the index or the position of the string characters

# str = "Chirag"

# print(str) # Chirag

# print(str.find("a")) # 4

# print(str.find('C')) # 0

# print(str.find("p")) # -1

# count() ------------------------------------------------------------------------------------------

# count() ---> which can be counting that how many characters of the string are present in the string

str = "Chirag Shrimali"

print(str) # Chirag Shrimali

print(str.count("i")) # 3

print(str.count('a')) # 2

print(str.count("d")) # 0
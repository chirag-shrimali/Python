# character users enters a to z or A to Z converts that characters into reverse form means a to A and A to a this is just a demo..

# ch = input("Enter the Character : ") # String data-types

# # the ascii value of a is 97
# # the ascii value of A is 65

# if(ch >= 'a' and ch <= 'z') :
#     ch = ord(ch) - 32
# else : # ch >= 'A' or ch <= 'Z'
#     ch = ord(ch) + 32

# print(chr(ch))

# users enters three numbers like a b and c checking the conditions that which numbers is larger medium and low(less)...

# a = int(input("Enter the No1 : "))
# b = int(input("Enter the No2 : "))
# c = int(input("Enter the No3 : "))

# if(a > b and a > c and b > c) :
#     print("A is Larger , B is Medium , C is Smaller...")
# elif a > b and a > c and c > b :
#     print("A is Larger , C is Medium , B is Smaller...")
# elif(b > a and b > c and a > c) :
#     print("B is Larger , A is Medium , C is Smaller...")
# elif b > a and b > c and c > a :
#     print("B is Larger , C is Medium , A is Smaller...")
# elif(c > a and c > b and a > b) :
#     print("C is Larger , A is Medium , B is Smaller...")
# elif c > a and c > b and b > a :
#     print("C is Larger , B is Medium , A is Smaller...")

# character = input("Enter a Character : ")

# # a ascii value 97 and A ascii value 65
# # 65 - 97 32 diff.

# if character >= 'A' and character <= 'Z' :
#     character = ord(character) + 32
# elif(character >= 'a' and character <= 'z') :
#     character = ord(character) - 32

# print(chr(character))

# Types of Comments : 

'''
There are having two types of comments :-
1. Single - Line Comments
2. Multi - Line Comments
'''

"""
This is also a syntax of multi-line comments but another...
"""

# Write a program to print Twinkle twinkle little star poem in python

'''print("\n++++++++++ Twinkle, Twinkle, Little Star ++++++++++")

print('\n                                     By Jane Taylor')

print("""\n
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark,
How could he see where to go,
If you did not twinkle so?

In the dark blue sky you keep,
Often through my curtains peep
For you never shut your eye,
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.""")'''

# REPL -- Read Evaluate Print Loop

# Module -- There are having two types of module :-
'''
1. Built-in Module --- Python code module pre-installed
2. External Module --- python code module externally-installed
'''

# import pyjokes

# joke = pyjokes.get_joke()

# print(joke)

# import pyttsx3

# print('Speaking...')

# pyttsx3.speak('Hello Chirag Nice to meet you how are you which fields you are working right now and what occassions ')

# import os

# dir_path = r'C:\Users\CHIRAG\OneDrive\Desktop'

# contents = os.listdir(dir_path)

# for i in contents :
#     print(i)

# This is a module of os which can be taken in external module through installing a module

# import os

# in this the directionary path given of a file folder

# d_p = r'C:\Users\CHIRAG\OneDrive\C++\Screenshots'

# calling a os module by taking contents as variable in directionary_path

# contents = os.listdir(d_p)

# prints this contents

# # print(contents)

# or by the loops of for prints it

# for item in contents :
#     print(item)

# Write a python program to add two numbers.

# a = 5
# b = 7

# c = a + b 
# print(c)

# a = int(input('Enter the No1 : '))
# b = int(input("Enter the No2 : "))

# c = pow(a , b)
# print("\nAddition is : ",c)

# Write a python program to find remainder when a number is divided by z

# no = int(input("Enter the No : "))

# z = int(input('Enter the value of Z that you want to divided a numbers : '))

# rem = no % z
# print("\nRemainder : ",rem)

# Check the type of variable assigned using input () function.

# a = input("Enter the Name : ")

# print(type(a))

# Use comparison operator to find out whether ‘a’ given variable a is greater than
# ‘b’ or not. Take a = 34 and b = 80

# a = 34
# b = 80
# # 34 > 80
# if b > a :
#     print('Yes')
# else :
#     print('No')

'''
Operations :-
1. Arithmetic -- + - % / pow(var_1 , var_2)
2. Assignment -- = +=(= var_name + 1) -=
3. Comparison -- Relational -- > >= < <= == !=
4. Logical and or not
'''

# Write a python program to find an average of two numbers entered by the user.

# a = int(input("Enter the No1 : "))
# b = int(input("Enter the No2 : "))

# total = a + b

# print("Total : ",total)

# avg = total/2

# print("Average : ",avg)

# Write a python program to calculate the square of a number entered by the user.

# no = int(input("Enter the No : "))

# # perimeter circumstances circumference -- 4 * no

# square = no * no

# print('\nSquare is : ',square,"\bcm2")

# m1 = int(input("Enter the marks_1 : "))
# m2 = int(input("Enter the marks_2 : "))
# m3 = int(input("Enter the marks_3 : "))
# m4 = int(input("Enter the marks_4 : "))
# # m5 = input("Enter the marks_5 : ")
# # m6 = input("Enter the marks_6 : ")
# # f7 = input("Enter the fruit_7 name : ")

# # list = [f1 , f2 , f3 , f4 , f5 , f6 , f7]

# list = [m1 , m2 , m3 , m4]

# # print(list.sort())

# for i in list :
#     print(list[i])

# print(list[0] + list[1] + list[2] + list[3])

# print(list)

# print(list[5])

# import pyjokes

# joke = pyjokes.get_joke()

# print(joke)

# import pyttsx3

# print('Speaking...')

# pyttsx3.speak('Hello,Chirag Shrimali')
# pyttsx3.speak('Hello,Dhwani Shrimali')
# pyttsx3.speak('Hello,Girish Shrimali')
# pyttsx3.speak('Hello,Priti Shrimali')
# pyttsx3.speak('Hello,Prafulla Shrimali')
# pyttsx3.speak('Hello,Barthdev Shrimali')
# pyttsx3.speak('Hello,Karan Basanti Shrimali')

# import os # This is a modules name as os

# dir_path = r'C:\Users\CHIRAG\OneDrive\Desktop\Css Project\images'
# This is a directionary Path of our folders and files

# contents = os.listdir(dir_path)
# contents name variable which can be stored the folder or file of the users enters url

# # print(contents) # prints contents

# for item in contents :
#     print(item)

# a = input("Enter a Number : ")
# print(type(input())) square area number * number square perimeter/circumstances/circumference 4 * number

# Write a program to find the greatest of four numbers entered by the user.

# a = int(input('Enter the No1 : '))
# b = int(input('Enter the No2 : '))
# c = int(input('Enter the No3 : '))
# d = int(input('Enter the No4 : '))
# # a = 5 ,b = 5 ,c = 5 ,d = 5 
# #  5 > 5 5 > 5 5 > 5
# if a > b and a > c and a > d :
#     print('A is Greatest...')
# elif b > a and b > c and b > d :
#     print("B is Greatest...")
# elif c > a and c > b and c > d :
#     print('C is Greatest...')
# # elif d > a and d > b and d > c :
# else :
#     print("D is Greatest...")

#Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

# sub1 = int(input("Enter the subject_1 Marks : "))
# sub2 = int(input("Enter the subject_2 Marks : "))
# sub3 = int(input("Enter the subject_3 Marks : "))

# total = sub1 + sub2 + sub3

# avg = total/3 # (sub1 + sub2 + sub3)/3

# print('\nThe Marks of Subject_1 :',sub1)
# print('The Marks of Subject_2 :',sub2)
# print('The Marks of Subject_3 :',sub3)

# print('\nTotal is :',total)
# print("Average of Total marks :",avg)

# if(avg >= 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33) :
#     print('Pass')
# else :
#     print('Fail')

# Write a program to find whether a given username contains less than 10
# characters or not.

# username = input("Enter the User_Name : ")

# if len(username) < 10 :
#     print('A given username contains less than 10 characters...')
# else :
#     print('''A given username can't contains less than 10 characters...''')

# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.

# sc1 = "Make a lot of money" # spam_comment_1
# sc2 = "buy now" # spam_comment_2
# sc3 = "subscribe this" # spam_comment_3
# sc4 = "click this" # spam_comment_4

# message = input("Enter the message of comment : ")

# if(sc1 in message or sc2 in message or sc3 in message or sc4 in message) :
#     print('Yes,a message can be contains a spam comment...')
# else :
#     print('No,a message can be contains a spam comment...')

# Write a program which finds out whether a given name is present in a list or not

# list = 0            1          2         3          4         5

# list = ["Chirag" , "Ruturaj" , "Dhoni" , "Jaddu" , "Shivam" , "Ayush"]

# name = input("Enter the User_Name : ")

# if(name in list) :
#     print('Yes, a lists contains a username that user enters...')
# else :
#     print('''No, a lists can't contains a username that user enters...''')

'''
Write a program to calculate the grade of a student from his marks from the
following scheme:
90 – 100 => Ex
80 – 90 => A
70 – 80 => B
60 – 70 =>C
50 – 60 => D
<50 => F
'''

# marks = int(input("Enter the Marks : "))

# if(marks >= 90 and marks < 100) :
#     grade = 'Ex'
#     print('Excellent Performance...')
# elif marks >= 80 and marks < 90 :
#     grade = "A"
# elif(marks >= 70 and marks < 80) :
#     grade = 'B'
# elif marks >= 60 and marks < 70 :
#     grade = "C"
# elif(marks >= 50 and marks < 60) :
#     grade = 'D'
# elif marks < 50 :
#     grade = 'F'
#     print('Fail Better luck next time!!')

# print("\nAccording to Your Marks you can be pass a exam with",grade,"grades")

# Write a program to find out whether a given post is talking about "Chirag" or not.

# post_talk = input("Enter the post_talking : ")

# if("chirag".lower() in post_talk.lower()) :
#     print('Yes,post can be talking about chirag Bhai...')
# else :
#     print('''No,post can't be talking about chirag Bhai...''')

# Write a program to find whether a given number is prime or not.

# no = int(input("Enter the No : "))

# count = 0

# for i in range(1 , no + 1) :
#     if(no % i == 0) :
#         count += 1 # count = count + 1

# if count == 2 :
#     print(no,"is a Prime No...")
# else :
#     print(no,"is not a Prime No...")

# whether check that users enters a numbers is prime or not...

# no = int(input("Enter the No : "))

# # 1 to 11 prints 1 to 10

# count = 0

# for i in range(1, no + 1) :
#     if(no % i == 0) :
#         count += 1

# if count == 2 :
#     print(no,'is a Prime No...')
# else :
#     print(no,"is not a Prime No...")

# no = int(input("Enter the No : "))

# for i in range(2 , no) :
#     if(no % i) == 0 :
#         print(no,"is not a prime No...")
#         break
# else :
#     print(no,"is a Prime No...") 

# no = int(input('Enter the No : '))

# count = 0

# for i in range(1 , no + 1) :
#     if(no % i == 0) :
#         count += 1 # count = count + 1

# if(count == 2) :
#     print(no,"is a Prime No...")
# else :
#     print(no,'is not a Prime No...')

# no = int(input('Enter the No : '))

# for i in range(2 , no) :
#     if(no % i) == 0 :
#         print(no,'is not a Prime No...')
#         break

# else :
#     print(no,'is a Prime No...')

# Write a program to find the sum of first n natural numbers using while loop.

# no = int(input('Enter the No : '))

# i = 1
# sum = 0

# while(i < no + 1) :
#     sum += i # sum = sum + i
#     print("\n",i)
#     i += 1 # i = i + 1

# print('\nThe Sum is :',sum)

# Write a program to calculate the factorial of a given number using for loop.

# no = int(input("Enter the No : "))

# fc = 1
# sum = 0

# for i in range(1 , no + 1) :
#     fc = fc * i # fc *= i
#     sum = sum + i # sum += i

# print('\nThe Factorai of',no,'is :',fc)
# print('\nThe Sum is :',sum)

# even or odd check

# no = int(input("Enter the No : "))

# if no % 2 != 0 :
#     print("\n",no,'is an Odd No...')
# else :
#     print("\n",no,"is an Even No...")

# birth_day = int(input("Enter Your Birth Date : "))

# birth_month_day = int(input('Enter Your Month Date : '))

# final_date = (((((birth_day * 2) + 5) * 50) + birth_month_day) - 250)

# print('\nThe Birth Date of Month is :',final_date)

'''
mul = b_d * 2
add = mul + 5
mul1 = add * 50 
add1 = mul1 + b_d_m
final = add1 - 250
'''

# Write a program to print multiplication table of a given number using for loop

# no = int(input("Enter the No : "))

# i = 10

# while(i > 0) :
#     print(f"{no} X {i} = {no * i}")
#     # print(no,"X",i,"=",no * i)
#     i -= 1 # i = i - 1

# for i in range(1 , 11) :
#     # print(no,"X",i,"=",no * i)
#     print(f"{no} X {11 - i} = {(11 - i) * no}")

# for i in range(1 , 11) :
    # print(no,"X",i,"=",no * i)
    # print(f"{no} X {i} = {no * i}")

'''
Write a program to greet all the person names stored in a list ‘l’ and which starts
with S.
l = ["Harry", "Soham", "Sachin", "Rahul"]
'''
# list = ["Harry", "Soham", "Sachin", "Rahul" , "Chirag" , "Shrimali" , "Chiku"]

# for name in list :
#     if(name.startswith("C")) :
#         print(f'Hello,{name}')

# ch = input('Enter a Character : ')

# if(ch >= 'A' and ch <= 'Z') :
#     ch = ord(ch) + 32
# else :
#     ch = ord(ch) - 32

# print(chr(ch))

# a = int(input('Enter the No1 : '))
# b = int(input('Enter the No2 : '))
# c = int(input('Enter the No3 : '))

# if a > b and a > c and b > c :
#     print('A is Big , B is Medium , C is Small...')
# elif a > b and a > c and c > b :
#     print('A is Big , C is Medium , B is Small...')
# elif b > a and b > c and a > c :
#     print('B is Big , A is Medium , C is Small...')
# elif b > a and b > c and c > a :
#     print('B is Big , C is Medium , A is Small...')
# elif c > a and c > b and a > b :
#     print('C is Big , A is Medium , B is Small...')
# elif c > a and c > b and b > a :
#     print('C is Big , B is Medium , A is Small...')

'''
    * i = 1
   *** i = 2 an = a + (n-1)d = 1 + (n-1)2 = 1 + 2n - 2 = 2n - 1
  ***** i = 3 for n = 3
'''

"""
* i = 1
** i = 2
*** i = 3 for n = 3
"""

# no = int(input('Enter the No : '))

# for i in range(1 , no + 1) :
#     # print(' ' * (no - i),end="")
#     print("*" * (i),end="")
#     print("")

'''
* * * i = 1
*   * i = 2   for n = 3
* * * i = 3
'''
# no = int(input('Enter the No : '))
# # 3 -- 1 4 -- 2 5 -- 3
# for i in range(1 , no + 1) :
#     if(i == 1 or i == no) :
#         print('*' * (no))
#         # print("")
#     else :
#         print('*',end="")
#         print(" " * (no - 2),end="")
#         print('*',end="")
#         print("")
#     # print("")

'''2i - 1
  * i = 1 -> 2 * 1 - 1 = 2 - 1 = 1
 *** i = 2 -> 2 * 2 - 1 = 4 - 1 = 3
***** i = 3 for n = 3 -> 2 * 3 - 1 = 6 - 1 = 5
'''

# no = int(input("Enter the No : "))

# for i in range(1 , no + 1) :
#     print(" " * (no - i),end="")
#     print("*" * (2 * i - 1),end="")
#     print("")

"""
* -> i = 1
** -> i = 2
*** -> i = 3 for no = 3
"""

# no = int(input('Enter the No : '))

# for i in range(1 , no + 1) :
#     print("*" * (i),end="")
#     print("")

'''
*** -> i = 1
* * -> i = 2
*** -> i = 3 for no = 3
'''

# no = int(input("Enter the No : "))

# for i in range(1 , no + 1) :
#     if(i == 1 or i == no) :
#         print("*" * (no),end="")
#         print("",end="")
#     else :
#         print("*",end="")
#         print(" " * (no - 2),end="")
#         print("*",end="")
#         print("",end="")
#     print("")

# # Check that a tuple type cannot be changed in python. tuples and strings are immutable means can not be changed in the existing tuples
# but the lists are mutable means can be changed a existing lists by their different different types of lists methods

#      0        1      2       3

# t = ("Chirag" , 21 , "Vgec" , 2147)

# print(t[1:3])
# print(type(t))

# t[0] = 'Chintu'
# t[1] = 20

# fruits 7 names lists displays

# fruits = []

# f1 = input("Enter the First Fruits Name : ")
# fruits.append(f1)
# f2 = input("Enter the Second Fruits Name : ")
# fruits.append(f2)
# f3 = input("Enter the Third Fruits Name : ")
# fruits.append(f3)
# f4 = input("Enter the Fourth Fruits Name : ")
# fruits.append(f4)
# f5 = input("Enter the Fifth Fruits Name : ")
# fruits.append(f5)
# f6 = input("Enter the Sixth Fruits Name : ")
# fruits.append(f6)
# f7 = input("Enter the Seventh Fruits Name : ")
# fruits.append(f7)

# # print(fruits) 
# print(fruits[0:7])

# Lists are mutable means in the existing lists we cane changed...

#       0      1       2     3        4      5

# list = [5 , 4 , 3 , 9 , 8 , 2]

# # print(list)
# # print(list[1:5])

# print(list)

# list.insert(2 , 7)

# print(list)

t = (3 , 7 , 1 , 4 , 5)

# print(len(t))

# l = len(t)

# print(l)

# t1 = (1 , 2)

# t2 = (3 , 4)

# t1 = (1 , 2 , 3)

# a , b , c = (1 , 2 , 3)

# print(a , b , c)

# t = (1 , 2 , 3) # Empty tuple

# print(t)
# print(type(t))

# print(t[1:4])

# print(max(t))
# print(min(t))



# con = t1 + t2

# print(con)

# mul = t1 * 4

# print(mul)

# print(3 in t1) # retrun False
# print(3 in t2) # return True

# cnt = t.count(5)

# idx = t.index(9)

# print(idx)

# print(cnt) 
# print(t.count(5))

# String / Tuples both are immutable means in the existing string or tuples we can not be changed
# but Lists are mutable means in the existing lists we can change it

# 0 --- C
# 1 --- h
# 2 --- i
# 3 --- r
# 4 --- a
# 5 --- g

# string = "5.5"

# print(type(string)) # <'str'>
# # print(string[2:5])

# c = string.translate("6.5")

# print(c)

# for i in string :
#     print(i)

#    0       1        2        3

# t = (21 , "Chirag" , 21.47 , 'Vgec')

# t[1] = 'Ramesh'

#       0       1         2       3       4

list = [21 , "Chirag" , 21.47 , False , 'Vgec']

# print(list)
# print(list[2])
# print(list[1])
# print(list[4])
# print(list[1:4]) # slicing the lists 0 which can be included in the lists where at the 5th index lists can not be included it's excluded

# Methods Lists :-
'''
1. Append -- at the last of the lists adding
2. Sort -- only numbers
3. Reverse -- numbers reverse
4. Remove -- elements index
5. Pop -- at the last remove delete idx remove
6. Insert -- at the first add otherwise idx add
'''
#       0   1   2   3   4   5
# list = [5 , 6 , 8 , 3 , 9 , 1]

# # print(list)
# # print(type(list))

# print(list)

# # list.reverse()
# # list.remove(8)
# # list.pop(2)
# # list.insert(2 , 10)

# print(list)

# tuple immutable existing tuple can not be changed
# t = (5 , 3 , 'Chintu' , "Vgec")

# print('--------------------------------')

# print(t)
# print(type(t))

# print('--------------------------------')

# t1 = () # empty tuples

# print(t1)
# print(type(t1))

# print('--------------------------------')

# t2 = (1) # single integer value can be stored in the tuple

# print(t2) # aana sivay badhu tuple bracket ma print thase
# print(type(t2)) # int

# print('--------------------------------')

# t3 = (1,) # single tuple example

# print(t3)
# print(type(t3))

# print('--------------------------------')

# t4 = (5 , 6 , 7 , 3) # multiple tuple can be stored in the tuple

# print(t4)
# print(type(t4))

# print('--------------------------------')

#    0   1      2          3

# t = (5 , 3 , 'Chintu' , "Vgec" , 3 , 6 , 5 , 3 , 9 , 3)

#   -4   -3     -2         -1

# print(t[-5])

# idx = t.index('Vgec')

# cnt = t.count(3)

# print(cnt)

# t1 = (1 , 3)
# t2 = (5 , 3)

# con = t1 + t2

# print(con)

# t1 = (1 , 2)

# mul = t1 * 3

# print(mul)

# t1 = (5 , 3 , 4 , 7)

# print(5 in t1) # True
# print(8 in t1) # False
# print(4 in t1) # True
# print(9 in t1) # False

# t1 = (5 , 8 , 3 , 9 , 7 , 6 , 4)

# print(len(t1))

#     0   1   2   3   4

# t1 = (1 , 5 , 3 , 7 , 2)

# print(t1[1:4])

# t1 = (1 , 2 , 5)

# a , b , c = (1 , 2 , 3)

# print(a , b , c)

# t1 = (5 , 9 , 3 , 4 , 7)

# print(min(t1))

# print(max(t1))

#         012345

"""
C -- 0 --> -6
h -- 1 --> -5
i -- 2 --> -4
r -- 3 --> -3
a -- 4 --> -2
g -- 5 --> -1

"""

# string = 'Chirag'

# print(string[4:1])

# string = 'Chirag'

"""
C -- 0 --> -6
h -- 1 --> -5
i -- 2 --> -4
r -- 3 --> -3
a -- 4 --> -2
g -- 5 --> -1 -- immutable string/tuple can not be changed in the existing tuple/string
lists are mutable can be changed the existing lists
"""

# print(type(string))
# print(string)

# for i in string :
#     print(i)
# print(string[3:6])

# str = 'Chirag'
# print(str)
# print(type(str))
# print('-----------------')
# str = "Chirag"
# print(str)
# print(type(str))
# print('-----------------')
# str = """Chirag"""
# print(str)
# print(type(str))
# print('-----------------')
# str = '''Chirag'''
# print(str)
# print(type(str))
# print('-----------------')

# string = 'C'

# print(len(string))
# print(type(string))

# loops three types for while while true

# string = 'Chirag' # hrg

# string[3] = "R"

# print(string[1:6:2])

# string are immutable can not be changed the existing string

""" -7 or 6 out of the range index 
C -- 0 --> -6
h -- 1 --> -5
i -- 2 --> -4
r -- 3 --> -3
a -- 4 --> -2
g -- 5 --> -1
len(string) = 6
"""

# print(len(string)) # 6
# print(string) # Chirag
# print(string[2]) # i
# print(string[-6]) # C
# print(string[0:6:2]) # Chirag -- Cia
# print(string[-6:-3]) # Slice methods Chirag

# str = 'Mathematics'

# print(str[2:9:2]) # themati --> teai

# print(string[:4]) # 0:4 --> Chir
# print(string[2:]) # 2:6 --> irag

# string = 'Chirag'

# print(len(string)) # 6
# print(string.lower()) # chirag
# print(string.upper()) # CHIRAG
# print(string.capitalize()) # Chirag shrimali bhai
# print(string.title()) # Chirag Shrimali Bhai

# print(string.startswith('Chi')) # True
# print(string.startswith('chi')) # False
# print(string.startswith('hi')) # False
# print(string.startswith('Ci')) # False

# print(string.endswith('rag')) # True
# print(string.endswith('g')) # True
# print(string.endswith('rg')) # False
# print(string.endswith('ag')) # True
# print(string.endswith('r')) # False

# str = "Chirag Shrimali" # only space is required no alphabets , sc , numeric numbers are have 

# # check = str.replace('Chirag' , "Rajesh")

# # check = str.replace("nice" , 'Bad')

# # print(check)

# f = str.find('mali')

# print(f)

# string = "Chirag \\is\na \t\"nice\" person"

# print(string)

# string and tuple are immutable means in the existing tuple -- () or string "" , '' , """ """ , ''' ''' can't be changed then
# lists are the mutable can be changing the existing lists []

# Check that a tuple type cannot be changed in python. 

#    0       1        2          3            4

# t = (21 , "Chirag" , 2147 , 'Chirag@0411' , "Vgec")

# t[1] = 'Ramesh' # tuple object can not be assignment item

# Write a python program to display a user entered name followed by Good Afternoon using input () function. 

# name = input('Enter the Name : ')

# print(f"Good Afternoon,{name}")

"""
Write a program to fill in a letter template given below with name and date. 
letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|>
'''
"""

# letter = '''  
#     Dear <|Name|>, 
# You are selected! 
#     <|Date|>
# '''

# print(letter.replace("<|Name|>" , 'Chirag').replace('<|Date|>' , "4th November,2025"))

# Write a program to detect double space in a string.

# Replace the double space from problem 3 with single spaces.

# string = 'This is a nice  person who are having good  gestures.'

# print(string.replace("  " , ' '))

'''
Write a program to format the following letter using escape sequence 
characters. 
letter = "Dear Harry, this python course is nice. Thanks!" 
'''

# letter = "\nDear Harry,\n\tThis python course is nice. \b\nThanks!"

# print(letter)

'''
column
      |
row - * * * * * i = 1 
      * * * * * i = 2
      * * * * * i = 3
      * * * * * i = 4
      * * * * * i = 5
'''

# no = int(input("Enter the No : "))

# for i in range(1 , no + 1) :
#     print("* " * (no),end="")
#     print("")

"""
column
       |
row -> * -> i = 1
       * * -> i = 2
       * * * -> i = 3
       * * * * -> i = 4
       * * * * * -> i = 5
"""

# no = int(input('Enter the No : '))

# for i in range(1 , no + 1) :
#     print('* ' * (i),end="")
#     print()

'''
column
       |
row -> * * * * * -> i = 5
       * * * * -> i = 4
       * * * -> i = 3
       * * -> i = 2
       * -> i = 1
'''

# no = int(input('Enter the No : '))

# for i in range(no , 0 , -1) :
#     print('* ' * (i),end="")
#     print("")

"""
column
        |
rows -> 1 -> i = 1
        1 2 -> i = 2
        1 2 3 -> i = 3
        1 2 3 4 -> i = 4
        1 2 3 4 5 -> i = 5
"""

'''
column
        |
rows -> 1 2 3 4 5 -> i = 5
        1 2 3 4 -> i = 4
        1 2 3 -> i = 3
        1 2 -> i = 2
        1 -> i = 1
'''

"""
column
        |
rows -> 5 4 3 2 1 -> i = 5
        5 4 3 2 -> i = 4
        5 4 3 -> i = 3
        5 4 -> i = 2
        5 -> i = 1
"""

'''
column
        |
rows -> 5 -> i = 1 
        5 4 -> i = 2
        5 4 3 -> i = 3
        5 4 3 2 -> i = 4
        5 4 3 2 1 -> i = 5
'''

# no = int(input("Enter the No : "))

# for i in range(1 , no + 1) :
#     for j in range(no , no - i , -1) :
#         print(j," ",end="")
#     print("")

"""
column
        |
rows -> a -> i = 1
        a b -> i = 2
        a b c -> i = 3
        a b c d -> i = 4
        a b c d e -> i = 5
"""

# no = int(input('Enter the No : '))

# for i in range(1 , no + 1) :
#     for j in range(1 , i + 1) :
#         print(chr(96 + j) , " " , end="")
#     print("")

'''
column
        |
rows -> 1 2 3 4 5 -> i = 5
        2 3 4 5 -> i = 4
        3 4 5 -> i = 3
        4 5 -> i = 2
        5 -> i = 1
'''

# no = int(input('Enter the No : '))

# for i in range(no , 0 , -1) :
#     for j in range(no - i + 1 , no + 1) :
#         print(j , " " , end="")
#     print()

'''
column
        |
rows -> 1 2 3 4 5 -> i = 5
        2 3 4 5 -> i = 4
        3 4 5 -> i = 3
        4 5 -> i = 2
        5 -> i = 1
'''

# no = int(input('Enter the No : '))

# for i in range(no , 0 , - 1) :
#     for j in range(no - i + 1 , no + 1) :
#         print(j , ' ' , end="")
#     print()

'''
* * *
*   *
* * *
*
* *
* * *
'''

# no = int(input('Enter the No : '))

# for i in range(1 , no + 1) :
#     print(' ' * (no - i) , end="")
#     print('* ' * (i) ,end="")
#     print("""""")

# for i in range(1 , no + 1) :
#     if i == 1 or i == no :
#         print('*' * (no) , end="")
#         print()
#     else :
#         print('*',end="")
#         print(' ' * (no - 2) , end="")
#         print('*' , end="")
#         print()
# #     print()

# Prime No or not
# no = int(input('Enter the No : '))

# count = 0

# for i in range(1 , no + 1) :
#     if(no % i == 0) :
#         count += 1 # count = count + 1

# if count == 2 :
#     print(no,'is a Prime No...')
# else :
#     print(no,"is not a Prime No...")

# no = int(input('Enter the No : '))

# for i in range(2 , no) :
#     if (no % i) == 0 :
#         print(no,'is not a Prime No...')
#         break

# else :
#         print(no,"is a Prime No...")

# Perfect no or not --> 6 , 28 6 factorial 1 , 3 , 2 , 6

# no = int(input('Enter the No : '))

# sum = 0

# for i in range(1 , no) :
#     if(no % i == 0) :
#         sum = sum + i

# if no == sum :
#     print(no,"is a Perfect No...")
# else :
#     print(no,'is not a Perfect No...')

# Checking that a number is armstrong or not -> 153 - 1 + 125 + 27 = 153

# no = int(input('Enter the No : ')) # 153 -- 3 , 36999 -- 5

# sum = 0

# digit = len(str(no))

# temp = no # 153

# for i in range(digit) : # 0 to 3 -- 0 1 2 # rem = 1 , sum = 153 , no = 0
#     rem = no % 10 # 153 % 10 = 3 --> 15 % 10 = 5 --> 1 % 10 = 1
#     sum = sum + pow(rem , digit) # 0 + pow(3 , 3) # 0 + 27 = 27 -> 27 + pow(5 , 3) = 27 + 125 = 152 -> 152 + pow(1 , 3) = 152 + 1 = 153
#     no = no//10 # 153//10 = 15 -> 15//10 = 1 -> 1//10 = 0

# if temp == sum :
#     print(temp,'is an Armstrong No...')
# else :
#     print(temp,"is not an Armstrong No...")

# checking that a number that enters by users is twin or not

# no = int(input('Enter the No : ')) # 123

# mul = 1
# sum = 0

# digit = len(str(no)) # 3 -- 0 to 3 -> 0 1 2

# temp = no

# for i in range(digit) :
#     rem = no % 10 # 3 2 1
#     sum = sum + rem # 0 + 3 --> 3 --> 3 + 2 = 5 --> 5 + 1 = 6
#     mul = mul * rem # 1 * 3 --> 3 * 2 = 6 --> 6 * 1 = 6
#     no = no//10 # 12 --> 1 --> 0

# if sum == mul :
#     print(temp,'is a Twin No...')
# else :
#     print(temp,"is not a Twin No...")
    
# check that number enter by user is reverse or not

# no = int(input('Enter the No : ')) # 1234

# rev = 0

# digit = len(str(no)) # 4 --> 0 to 4 --> 0 1 2 3

# for i in range(digit) :
#     rem = no % 10 # 1234 % 10 --> 4 --> 123 % 10 --> 3 --> 12 % 10 --> 2 --> 1 % 10 --> 1
#     rev = (rev * 10) + rem # (0 * 10) + 4 --> 4 --> (4 * 10) + 3 == 40 + 3 = 43 --> (43 * 10) + 2 --> 430 + 2 --> 432 --> (432 * 10) + 1 --> 4320 + 1 --> 4321
#     no = no//10 # 1234//10 --> 123 --> 123//10 --> 12 --> 12 //10 --> 1 --> 1 // 10 --> 0

# print("\nThe Reverse Value is :",rev)

# checking that user enters a number palindrome or not

# no = int(input('Enter the No : ')) # 121

# rev = 0

# digit = len(str(no)) # 3 --> 0 to 3 --> 0 1 2

# temp = no

# for i in range(digit) : # 0
#     rem = no % 10 # 121 % 10 --> 1 --> 12 % 10 --> 2 --> 1 % 10 --> 1
#     rev = (rev * 10) + rem # (0 * 10) + 1 --> 1 --> (10) + 2 --> 12 --> (12 * 10) + 1 = 120 + 1 ==> 121
#     no = no//10 # 121//10 --> 12 --> 12//10 --> 1 --> 1//10 = 0

# if temp == rev :
#     print(temp,'is a Palindrome No...')
# else :
#     print(temp,"is not a Palindrome No...")

# finding a factorial of a number that enters by users and also sum of n natural number that enters by users of that numbers

# no = int(input('Enter the No : ')) # 4 

# fc = 1
# sum = 0

# for i in range(1 , no + 1) : # 1 to 5 --> 1 2 3 4
#     fc = fc * i # 1 * 1 = 1 --> 1 * 2 = 2 --> 2 * 3 = 6 --> 6 * 4 = 24
#     sum = sum + i # 0 + 1 = 1 --> 1 + 2 = 3 --> 3 + 3 = 6 --> 6 + 4 --> 10

# print('\nThe Factorial of',no,'natural numbers are :',fc)
# print('\nThe Sum of',no,"natural numbers are :",sum)

# prints the multiplication table of the number that enters by users

# no = int(input('Enter the No : '))

# print('\nThe Multiplication Table of',no,"are : ")

# # i = 10

# # while(i > 0) :
# #     print("\n",no,'X',i,"=",(no * i))
# #     i -= 1 # i = i - 1

# for i in range(1 , 11) :
#     print(f"\n{no} X {11 - i} = {(11 - i) * no}")


# checking that user enters a number is strong krishnamurthy or factorion number or not

# no = int(input('Enter the No : ')) # 145 --> 1! + 4! + 5! = 1 + 24 + 120 = 145 no == fc(sum)

# digit = len(str(no)) # 145 --> 3

# sum = 0
# temp = no # temp = 145

# for i in range(digit) : # 145 --> 3 --> 0 to 3 --> 0 1 2
#     rem = no % 10 # 145 % 10 --> 5 --> 14 % 10 --> 4 --> 1
#     fc = 1
#     for j in range(1 , rem + 1) : # 1 to 6 --> 1 2 3 4 5
#         fc = fc * j # 1 * 1 --> 1 --> 2 --> 6 --> 24 --> 120
#     sum = sum + fc # 0 + 1 --> 1 --> 3 --> 9 --> 33
#     no = no//10 # 145//10 --> 14 --> 1 --> 0

# if temp == sum :
#     print(temp,'is a Strong No...')
# else :
#     print(temp,"is not a Strong No...")

# checking that user enters a number is strong krishnamurthy factorion number or not

# no = int(input('Enter the No : '))

# sum = 0

# digit = len(str(no))

# temp = no

# for i in range(digit) :
#     fc = 1
#     rem = no % 10
#     for j in range(1 , rem + 1) :
#         fc = fc * j
#     sum = sum + fc
#     no = no//10

# if temp == sum :
#     print(temp,'is a Strong No...')
# else :
#     print(temp,"is not a Strong No...")

"""
* * * * * -> i = 1
* * * * * -> i = 2
* * * * * -> i = 3
* * * * * -> i = 4
* * * * * -> i = 5

* * * -> i = 1
*   * -> i = 2
* * * -> i = 3
****
*  *
*  *
****
"""

# no = int(input('Enter the No : '))

# for i in range(1 , no + 1) :
#     if(i == 1 or i == no) :
#         print('*' * (no) , end="")
#         print()
#     else :
#         print('*' , end="")
#         print(' ' * (no - 2) , end="")
#         print('*' ,end="")
#         print()

'''
* -> i = 1
* * -> i = 2
* * * -> i = 3
  * -> i = 1
 * * -> i = 2
* * * -> i = 3

* * * -> i = 1 
* * -> i = 2
* -> i = 3
'''

# no = int(input('Enter the No : '))

# for i in range(no , 0 , - 1) :
#     print('* ' * (i) , end="")
#     print()

# no = int(input('Enter the No : '))

# for i in range(1 , no + 1) :
#     print(' ' * (no - i) , end="") # 3 - 1 = 2 # 3 - 2 = 1 3 - 3 = 0
#     print('* ' * (i) ,end="")
#     print()

"""
1 -> i = 1
1 2 -> i = 2
1 2 3 -> i = 3
1 2 3 4 - > i = 4
1 2 3 4 5 -> i = 5

1 2 3 4 5 - > i = 5
1 2 3 4 -> i = 4
1 2 3 -> i = 3
1 2 -> i = 2
1 -> i = 1

5 4 3 2 1 -> i = 5
5 4 3 2 -> i = 4
5 4 3 -> i = 3
5 4 -> i = 2
5 -> i = 1

5
5 4
5 4 3
5 4 3 2
5 4 3 2 1

a -> i = 1
a b -> i = 2
a b c -> i = 3
a b c d -> i = 4
a b c d e -> i = 5
"""

# no = int(input('Enter the No : '))

# for i in range(1 , no + 1) :
#     for j in range(1 , i + 1) :
#         print(chr(96 + j) , ' ' , end="")
#     print()

# no = int(input('Enter the No : '))

# for i in range(1 , no + 1) : # 5 to 0 -> 5 4 3 2 1
#         for j in range(no , no - i , -1) : # 5 to 0 ->  
#                 print(j , ' ' , end="")
#         print()

'''
5 4 3 2 1 -> i = 5
5 4 3 2 -> i = 4
5 4 3 -> i = 3
5 4 -> i = 2
5 -> i = 1

5 -> i = 1
5 4 -> i = 2
5 4 3 -> i = 3
5 4 3 2 -> i = 4
5 4 3 2 1 -> i = 5
'''

# no = int(input('Enter the No : '))

# for i in range(1 , no + 1) :
#     for j in range(no , no - i  , -1) :
#         print(j , " " , end="")
#     print()

"""
1 2 3 4 5 -> i = 5
2 3 4 5 -> i = 4
3 4 5 -> i = 3
4 5 -> i = 2
5 -> i = 1
"""

# no = int(input('Enter the No : '))

# # for i in range(no , 0 , -1) :
# #     for j in range(no - i + 1 , 0 , -1) :
# #         print(j , ' ' , end="")
# #     print()

# for i in range(no , 0 , -1) : # 5 to 0 --> 5 4 3 2 1
#     for j in range(no - i + 1 , no + 1) : # 5 - 5 + 1 , 5 - 4 + 1 --> 2 , 5 - 3 + 1 = 3 , 5 - 2 + 1 = 4 , 5 - 1 + 1 = 5 
#         print(j , ' ' , end="")
#     print()

# no = int(input('Enter the No : '))

# count = 0

# for i in range(1 , no + 1) :
#     if no % i == 0 :
#         count += 1 # count = count + 1

# if (count == 2) :
#     print(no,'is a Prime No...')
# else :
#     print(no,"is not a Prime No...")

# for i in range(2 , no) :
#     if no % i == 0 :
#         print(no,'is not a Prime No...')
#         break
# else :
#     print(no,"is a Prime No...")

# Strong No/Krishnamurthy No/Factorion No

# no = int(input('Enter the No : '))

# sum = 0

# digit = len(str(no))

# temp = no

# for i in range(digit) :
#     fc = 1
#     rem = no % 10
#     for j in range(1 , rem + 1) :
#         fc = fc * j # fc *= j
#     sum = sum + fc # sum += fc
#     no = no//10 # no //= 10

# if sum == temp :
#     print(temp,"is a Strong No...")
# else :
#     print(temp,'is not a Strong No...')
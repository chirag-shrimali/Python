# Write a program to accept marks of 6 students and display them in a sorted manner.

s1_marks = int(input("Enter the Marks of Student_1 : "))
s2_marks = int(input("Enter the Marks of Student_2 : "))
s3_marks = int(input("Enter the Marks of Student_3 : "))
s4_marks = int(input("Enter the Marks of Student_4 : "))
s5_marks = int(input("Enter the Marks of Student_5 : "))
s6_marks = int(input("Enter the Marks of Student_6 : "))

#         0          1          2           3          4          5        

list = [s1_marks , s2_marks , s3_marks , s4_marks , s5_marks , s6_marks]

print('\nBefore Sorting : ')

print(list) # print(list[0:6])

list.sort()

print('\nAfter Sorting : ')

print(list[0:6]) # print(list)

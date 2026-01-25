# calculate grade of the students based on the marks

"""
marks >= 90 , grade = 'A'

90 > marks >= 80 , grade = 'B'

80 > marks >= 70 , grade = 'C'

70 > marks , grade = 'D'
"""

marks = int(input("\nEnter your Marks : "))

if(marks >= 90) :
    print("\nYou are passing the exam with A Grade...")
elif 90 > marks >= 80:
    print("\nYou are passing the exam with B Grade...")
elif (80 > marks >= 70):
    print("\nYou are passing the exam with C Grade...")
else :
    print("\nYou are passing the exam with D Grade.So,you are become fail in your exam...")
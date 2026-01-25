# Calculate the grade of a student from his marks from the following schema :
'''
90-100 --> Ex
80-90 --> A
70-80 --> B
60-70 --> C
50-60 --> D
<50 --> F
'''

marks = int(input("Enter Your Marks : "))

if(marks >= 90 and marks < 100) :
    grade = "Ex"
    print("Excellent Performance...")

elif(marks >= 80 and marks < 90) :
    grade = "A"

elif(marks >= 70 and marks < 80) :
    grade = "B"

elif(marks >= 60 and marks < 70) :
    grade = "C"

elif(marks >= 50 and marks < 60) :
    grade = "D"

elif(marks < 50) :
    grade = "F"
    print('You Become Fail...So,better luck next time!!')

print("You have passing this exam with",grade,"grades.")
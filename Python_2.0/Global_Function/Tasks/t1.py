'''

students = {"amit" : 25 , "summit" : 24 , "raj" : 23 , "ajay" : 24 , "sanjay" : 23}

bonus = False > 24 [1]

flag = False > 20 []

'''

students = {"amit" : 25 , "summit" : 24 , "raj" : 23 , "ajay" : 24 , "sanjay" : 23}

bonus = any(marks > 24 for marks in students.values())

flag = all(marks > 20 for marks in students.values())

print(f"BONUS : {bonus}")

print(f"FLAG : {flag}")
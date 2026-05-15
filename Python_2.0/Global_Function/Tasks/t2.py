# Dictionary Task :-

students = {"amit" : 89 , "summit" : 44 , "raj" : 99 , "ajay" : 69 , "jay" : 56}

print(students)

# reversing the items based on the marks with sorting...

# revSortedMarks = sorted(students.items() , key = lambda x : x[1] , reverse = True)

# sorting the items based on the names with sorting...

revSortedMarks = sorted(students.items() , key = lambda x : x[0])

print(revSortedMarks)
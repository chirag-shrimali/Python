'''  
task  :2 
Write a Python program to find strings in a given list containing a given substring.

Input:
[(ca,('cat', 'car', 'fear', 'center'))]

Output:
['cat', 'car']
'''

item = [('ca',('cat', 'car', 'fear', 'center' , 'ca'))]

item1 = []

for i in item :
    substring = i[0]
    string = i[1]

    for j in string :
        if substring in j :
            item1.append(j)

print(item1)
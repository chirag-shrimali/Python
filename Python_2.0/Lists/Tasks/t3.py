color = ["red" , "pink" , "yellow" , "blue" , "white" , "yellow" , "white" , "pink"]

list = []

dup = []

count = 0

for i in color :
    if i not in list :
        list.append(i)
    else :
        dup.append(i)
        count += 1
        dup.count(i)

print(list)
print(dup)
print("The Count are :",count)
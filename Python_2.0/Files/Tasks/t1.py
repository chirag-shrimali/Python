items = {'name' : "Chirag" , 'age' : 21 , 'city' : "Ahmedabad" , 'Country' : "India" , 'Marks' : 99}

# print(items)

file = open("Task1.txt" , "w")

for i in items :

    file.write(f"Name : {items['name']}\n")

    file.write(f"Age : {items['age']}\n")

    file.write(f"City : {items['city']}\n")

    file.write(f"Country : {items['Country']}\n")

    file.write(f"Marks : {items['Marks']}")

    break

file.close()
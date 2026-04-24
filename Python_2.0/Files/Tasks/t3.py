'''

items = {"name" : "Chirag" , 'age' : 21 , "city" : "Gujarat" , "Country" : "India" , "Marks" : 99 , "Hobby" : "Playing Cricket , Reading , Coding , ... , etc."}

file = open("Task.txt" , "w")

file.write(f"Name : {items['name']}\n")

file.write(f"Age : {items['age']}\n")

file.write(f"City : {items['city']}\n")

file.write(f"Country : {items['Country']}\n")

file.write(f"Marks : {items['Marks']}\n")

file.write(f"Hobbies : {items['Hobby']}")

file.write('\n\n--------------------------------------------------------------------\n\n')

file.close()

'''

while True :

    name = input("\nEnter the User Name : ")

    if name == "exit" :

        break

    else :

        file = open("Task.txt" , "a")

        file.write(f"\nName : {name}\n")

        file.close()
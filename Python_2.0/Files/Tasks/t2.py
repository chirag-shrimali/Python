while True :

    name = input("Enter the User Name : ")

    if name == "exit" :

        break
    
    else :

        file = open("Task2.txt" , "a")

        file.write(f"Name : {name}\n")

        file.close()
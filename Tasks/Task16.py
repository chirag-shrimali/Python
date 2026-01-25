# finds out whether a given name is present in a list or not

list = ["Chirag" , "Ramesh" , "Suresh" , "Mukesh" , "Krishna" , "Ram" , "Mahadev" , "Ganesh" , "Vishnu"]

name = input("Enter Your Name : ")

if(name.capitalize() in list) :
    print("Yes,your name is present in this list...")

else :
    print("No,your name is not present in this list...")
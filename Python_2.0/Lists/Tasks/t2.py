# List Program

list = ['red' , 'white' , "pink" , 'orange' , "green" , 'cyan' , 'black' , "blue" , 'yellow' , "purple"]

name_color = input("\nEnter the Color : ").lower()

for i in list :
    if(name_color in list) :
        list.remove(name_color)
        print(list)
        break
    else :
        print("\nEntered Color name are not to be found...")
        break
'''

in the file handling ,

there are write mode , read mode , append mode , w+ , r+ , a+ , ...

'''

name = "Chirag"

file = open("t1.txt" , "w")

'''

file.write("Hello , World !!\n")

file.write("My name is Chirag...\n")

file.write("I am a B.e. / B.tech Student Studying in Vgec...")

file.close()

'''

# Using Formatted String...

file.write(f"Hello , {name}\n")

file.close()
'''

in the file handling ,

there are write mode , read mode , append mode , w+ , r+ , a+ , ...

'''

# name = "Chirag"

# file = open("t1.txt" , "w")

'''

file.write("Hello , World !!\n")

file.write("My name is Chirag...\n")

file.write("I am a B.e. / B.tech Student Studying in Vgec...")

file.close()

'''

# -----------------------------------------------------------------------------------------------

# Using Formatted String...

# name = "Chirag"

# file = open("t1.txt" , "w")

# file.write(f"Hello , {name}\n")

# file.close()

# -----------------------------------------------------------------------------------------------


name = "Chirag"

file = open("t1.txt" , "w")

file.write(f"\nHello , {name} !!!")

print(f"\nHello , {name} !!" , file = file)

file.close()

# file.write(f"Hello!!") # We can not write after the file closing.it will be shows the error like I/O operation on closed file.

# ------------------------------------------------------------------------------------------------

# name = "Chirag"

# with open("t1.txt" , "w") as f :

#     f.write(f"Hello , {name}")

#     # f.close() # not required because the blocks with by default closed...
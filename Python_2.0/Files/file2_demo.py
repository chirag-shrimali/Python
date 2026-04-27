# in the files we can also read them...(READ MODE)

# file = open("Task.txt" , "r")

# read = file.read() # it will be prints the entire contexts of the files...

# print(read)

# -----------------------------------------------------------

# file = open("Task.txt" , "r")

# # read = file.read(10) # it will be prints the total number of characters from the beginning...

# read = file.read(20)

# print(read)

# ------------------------------------------------------------

# with open("Task.txt" , "r") as file :

#     read = file.read()

#     print(read)

# ------------------------------------------------------------

# with open("Task.txt" , "r") as file :

#     read = file.read(25)

#     print(read)

# -------------------------------------------------------------

# file = open("Task.txt" , "r")

# read = file.readline() # it will be displays the one single statements with \n...

# print(read)

# --------------------------------------------------------------

# with open("Task.txt" , "r") as file :

#     while True :

#         read = file.readline() # display and prints only one single line with \n...

#         print(read)

#         if not read :

#             break

# --------------------------------------------------------------

with open("Task.txt" , "r") as file :

    for i in file.readline() : # display and prints only one single line with \n...

        print(i)
import os

# it will be removing the files which can be exists in the folder...

# os.remove("deleteDemo.txt")

# print("Deleted...")

# ---------------------------------------------------------------------------------

# it will be check that given file name is exists in the folder if yes return true otherwise false...

# ans = os.path.exists("Rohit.txt")

# print(ans)

# ans = os.path.exists("Rohit1.txt")

# print(ans)

# print(os.path.exists("Rohit1.txt"))

# ------------------------------------------------------------------------------------

if os.path.exists("deleteDemo.txt") :

    os.remove("deleteDemo.txt")

    print("File can be deleted successfully!!")

else :

    print("File Path not Found...")
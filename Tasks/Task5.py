import os

# update this path correctly
directory_path = r'C:\Users\CHIRAG\OneDrive\Desktop\Python\Tasks'

contents = os.listdir(directory_path)

for item in contents:
    print(item)

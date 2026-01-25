#Converts Upper Alphabets to Smaller 
#Also,Lower Alphabets to Upper

character = input("Enter the Character : ")

# Ascii Value of A -- 65 ,a -- 97 diff. 97 - 65 = 32

if character >= 'A' and character <= 'Z' :
    character = ord(character) + 32
elif character >= 'a' and character <= 'z' :
    character = ord(character) - 32

print(chr(character))

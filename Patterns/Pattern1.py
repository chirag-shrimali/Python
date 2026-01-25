# Prints the following pattern :-

"""
    column
      |
row - * * * * * i = 1 
      * * * * * i = 2
      * * * * * i = 3
      * * * * * i = 4
      * * * * * i = 5
"""

no = int(input("Enter the No : "))

for i in range(1 , no + 1) :
    print("* " * (no),end="")
    print()
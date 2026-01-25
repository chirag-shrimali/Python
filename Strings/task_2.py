"""
task : 4 
take list from user append all element in list and print pelindorme word in list  
         input : ["java", "python", "php","cpp","flutter","maam"]
         output :  ['php','maam']
"""

e1 = input("Enter the First Elements : ")
e2 = input("Enter the Second Elements : ")
e3 = input("Enter the Third Elements : ")
e4 = input("Enter the Fourth Elements : ")
e5 = input("Enter the Fifth Elements : ")
e6 = input("Enter the Sixth Elements : ")

list = [e1 , e2 , e3 , e4 , e5 , e6]

print(list)

list1 = []

for i in list :
    if(i == i[ : : -1]) :
        list1.append(i)

print("\nThe Palindrome Word is :",list1)
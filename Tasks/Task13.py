# Checking a Student Pass or Fail

maths = int(input("Enter the marks of Maths Subject : "))

science = int(input("Enter the marks of Science Subject : "))

english = int(input("Enter the marks of English Subject : "))

total = maths + science + english

print("Marks of Maths Subject are :",maths)
print("Marks of Science Subject are :",science)
print("Marks of English Subject are :",english)
print("Total of three subjects are :",total)
# Extra things that can be also doing and that is to take averages 

avg = total/3
print("Averages of three subjects are :",avg)

if(avg >= 40 and maths >= 33 and science >= 33 and english >= 33) :
    print('Pass')

else :
    print('Fail')
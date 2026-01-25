# write the python program to take as two numbers as the input and calculate it's sum , diff , mul , div , mod , power

a = int(input("Enter the Value of No1 : "))

b = int(input('\nEnter the Value of No2 : '))

# whether check that user entering two numbers in which the first number is greater than the seconder

print(a > b) # return True if conditions satisfying otherwise returning False

# Sum----------------------------------------------------------

sum = a + b

print("\nThe Sum of Two Numbers are :",sum)

# Sub/Diff----------------------------------------------------------

sub = a - b

print("\nThe Subtraction of Two Numbers are :",sub)

# Mul----------------------------------------------------------

mul = a * b

print("\nThe Multiplication of Two Numbers are :",mul)

# Div----------------------------------------------------------

div = a / b

print("\nThe Division of Two Numbers are :",div)

# Mod----------------------------------------------------------

mod = a % b

print("\nThe Remainder of Two Numbers are :",mod)

# Power----------------------------------------------------------

power = a ** b

print("\nThe Power of Two Numbers are :",power)
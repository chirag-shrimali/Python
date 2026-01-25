# finding the factorial of n natural numbers as users enters
# Extra also calculate the sum of n natural numbers

no = int(input("Enter the Number : "))

fc = 1
sum = 0

for i in range(1 , no + 1) :
    fc = fc * i # fc *= i
    sum = sum + i # sum += i

print("\nThe Sum is :",sum)
print("The Factorial is :",fc)
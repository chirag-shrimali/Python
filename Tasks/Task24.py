# Calculate the sum of first n natural numbers using while loops

no = int(input("Enter the Number : "))

sum = 0
i = 1

while(i < no + 1) :
    sum = sum + i # sum += i
    print("\n",i)
    i += 1 # i = i + 1

print("\nThe Sum of first",no,"numbers are :",sum) 
# displays the sales of 4 to 5 days and then after the 30% discount shows in the list...

sales = [10 , 45 , 63 , 78 , 92]

sales1 = map(lambda x : x - x * 0.3 , sales)

print("Before Discount...")

print(sales)

print("After Discount...")

print(list(sales1))
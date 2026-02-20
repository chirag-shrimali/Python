# using while loop empty the dictionary and remove the items...

data = {1 : "Chirag" , 2 : "Ramesh" , 3 : "Suresh"}

while data :

    removeEle = data.popitem()

    print(f"{removeEle[0]} - {removeEle[1]}")

print(data)
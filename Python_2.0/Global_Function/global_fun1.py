# ZIP Function which can be sequentially displays the data of the users with multiple lists...

users = ["Chirag" , "Ramesh" , "Kartik" , "Shyam"]

marks = [99 , 94 , 78 , 69]

age = [19 , 25 , 36 , 17]

for i , j , k in zip(users , marks , age) :

    print(f"{i} - {j} - {k}")

# if users enter very much data in some lists when in second lists the data is less it will be skips
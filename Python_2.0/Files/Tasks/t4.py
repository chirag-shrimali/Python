'''
data = {"rohit":[100,20,121],"Virat":[90,98,78],"Kl":[151,89,7]}

op:

Score:

Player Name : rohit
Match 1:100
Match 2:20
Match 3:121

toal : 241

Player Name : rohit
Match 1:100
Match 2:20
Match 3:121

total : 241


Player Name : rohit
Match 1:100
Match 2:20
Match 3:121

total : 241

total score - 1000
'''

data = {"rohit" : [100 , 20 , 121] , "Virat" : [90,98,78] , "Kl" : [151 , 89 , 7]}

file = open("Task3.txt" , "w")

rows = []

colums = []

total = 0

for i , j in data.items() :

    # file.write(f"Player Name : {data['rohit']}")

    colums.append(j)

    rows.append(i)

total = sum(colums[0]) + sum(colums[1]) + sum(colums[2])

rohit = open("Rohit.txt" , "w")

print(rohit.write(f"Player Name : {rows[0]}\nMatch 1 : {colums[0][0]}\nMatch 2 : {colums[0][1]}\nMatch 3 : {colums[0][2]}\n\nTotal : {sum(colums[0])}\n\n"))

virat = open("Virat.txt" , "w")

print(virat.write(f"Player Name : {rows[1]}\nMatch 1 : {colums[1][0]}\nMatch 2 : {colums[1][1]}\nMatch 3 : {colums[1][2]}\n\nTotal : {sum(colums[1])}\n\n"))

# file.write(f"Total Score : {total}")

kl = open("KL.txt" , "w")

print(kl.write(f"Player Name : {rows[2]}\nMatch 1 : {colums[2][0]}\nMatch 2 : {colums[2][1]}\nMatch 3 : {colums[2][2]}\n\nTotal : {sum(colums[2])}\n\n"))
# Write a Python Program to make the rock(stone) / paper and scissors game using python

"""
import random which will be generate the random choice of (Rock / Paper / Scissors)

input user choice

1. Rock
Rock - Rock --> Tie!
Rock - Paper --> Paper Win! (Paper Covering Rock)
Rock - Scissors --> Rock Win! (Rock Samshes Scissors)

2. Paper
Paper - Paper --> Tie!
Paper - Rock --> Paper Win! (Paper Covering Rock)
Paper - Scissors --> Scissors Win! (Scissors Cut Paper)

3. Scissors
Scissors - Scissors --> Tie!
Scissors - Rock --> Rock Win! (Rock Samshes Scissors)
Scissors - Paper --> Scissors Win! (Scissors Cut Paper)
"""

import os
os.system('cls' if os.name == 'nt' else 'clear')

print(r"""
██████╗  ██████╗  ██████╗██╗  ██╗
██╔══██╗██╔═══██╗██╔════╝██║ ██╔╝
██████╔╝██║   ██║██║     █████╔╝ 
██╔══██╗██║   ██║██║     ██╔═██╗ 
██║  ██║╚██████╔╝╚██████╗██║  ██╗
╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝

██████╗  █████╗ ██████╗ ███████╗██████╗ 
██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██████╔╝███████║██████╔╝█████╗  ██████╔╝
██╔═══╝ ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
██║     ██║  ██║██║     ███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝

███████╗ ██████╗██╗███████╗███████╗ ██████╗ ██████╗ ███████╗
██╔════╝██╔════╝██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝
███████╗██║     ██║███████╗███████╗██║   ██║██████╔╝█████╗  
╚════██║██║     ██║╚════██║╚════██║██║   ██║██╔══██╗██╔══╝  
███████║╚██████╗██║███████║███████║╚██████╔╝██║  ██║███████╗
╚══════╝ ╚═════╝╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
""")
print("        ✊  📄  ✂   Let the battle begin!   ✊  📄  ✂\n")

import random as r

user_score = 0
comp_score = 0
count = 0

while count < 10 :
    user_choice = input("\nEnter Your Choice (Rock / Paper / Scissors) : ").lower()
    comp_choice = r.choice(['rock' , 'paper' , 'scissors'])

    if user_choice not in ('rock' , 'paper' , 'scissors') :
        print("\nInvalid Choice Of Selection!!")
        continue

    print("\nThe User Choice is :",user_choice)

    print("\nThe Computer Choice is :",comp_choice)

    count += 1 # count = count + 1 --> 0 to 10 times iterable

    if(user_choice == comp_choice) :
        print("\nBoth Select Same Choice!! The Match become Tie!!")
        user_score += 1
        comp_score += 1

    elif user_choice == "rock" :
        if comp_choice == "paper" :
            print("\nPaper Win! (Paper Covering Rock)")
            comp_score += 1
        
            print("\nComputer Win!!")

        else :
            print("\nRock Win! (Rock Samshes Scissors)")
            user_score += 1

            print("\nUser Win!!")

    elif user_choice == 'paper' :
        if comp_choice == "rock" :
            print("\nPaper Win! (Paper Covering Rock)")
            user_score += 1

            print("\nUser Win!!")

        else :
            print("\nScissors Win! (Scissors Cut Paper)")
            comp_score += 1

            print("\nComputer Win!!")

    elif user_choice == "scissors" :
        if comp_choice == "rock" :
            print("\nRock Win! (Rock Samshes Scissors)")
            comp_score += 1

            print("\nComputer Win!!")

        else :
            print("\nScissors Win! (Scissors Cut Paper)")
            user_score += 1

            print("\nUser Win!!")

# Final Result Match Score

print("\n=========================== FINAL MATCH SCORE RESULT ======================================\n")

print("\nThe User Total Score are :",user_score)

print("\nThe Computer Total Score are :",comp_score)

if(user_score > comp_score) :
    print("\nThe Winner is User!! User Win!!")

elif comp_score > user_score :
    print("\nThe Winner is Computer!! Computer Win!!")

else :
    print("\nBoth Computer and User Win!! Match becomes Tie!!")
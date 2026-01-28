# Write the python program to make the program of rock , paper and scissors

print("\n########## ROCK / PAPER / SCISSORS ##########")

import random as r

user_score = 0

comp_score = 0

count = 0

while count < 11 :

    user_choice = input("\nEnter Your Choice (Rock , Paper and Scissors) : ").lower()

    result = r.choice(['rock' , 'paper' , 'scissors'])

    if user_choice not in ['rock' , 'paper' , 'scissors'] :
         print("\nInvalid Choice of Selection!!")
         continue
    
    print("\nThe User Choice is :",user_choice.lower())

    print("\nThe Computer Choice is :",result.lower())

    count += 1

    if(user_choice == result) :
        print('\nTie!!')
        comp_score += 1
        user_score += 1
        print("\nUser Score :",user_score)
        print("\nComputer Score :",comp_score)

    elif user_choice == 'rock' and result == "scissors":
        print('\nUser Win!!')
        user_score += 1
        print("\nUser Score :",user_score)
        print("\nComputer Score :",comp_score)
        
    elif result == 'rock' and user_choice == "scissors":
        print('\nComputer Win!!')
        comp_score += 1
        print("\nUser Score :",user_score)
        print("\nComputer Score :",comp_score)
        
    elif user_choice == 'scissors' and result == "paper" :
        print('\nUser Win!!')
        user_score += 1
        print("\nUser Score :",user_score)
        print("\nComputer Score :",comp_score)
        
    elif result == 'scissors' and user_choice == "paper" :
        print('\nComputer Win!!')
        comp_score += 1
        print("\nUser Score :",user_score)
        print("\nComputer Score :",comp_score)
        
    elif user_choice == 'paper' and result == "rock" :
        print('\nUser Win!!')
        user_score += 1
        print("\nUser Score :",user_score)
        print("\nComputer Score :",comp_score)
        
    elif result == 'paper' and user_choice == "rock" :
        print('\nComputer Win!!')
        comp_score += 1
        print("\nUser Score :",user_score)
        print("\nComputer Score :",comp_score)

print("\n=============================================================")

print("\nThe Final Result Score are :")

print("\nThe User Score is :",user_score)

print("\nThe Computer Score is :",comp_score)

if(user_score == comp_score) :
        print("\nTie!! Both Win")
elif user_score > comp_score :
        print("\nUser Win!!")
else :
        print("\nComputer Win!!")
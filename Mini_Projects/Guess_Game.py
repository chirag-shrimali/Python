# Write the Python Program in which we have to make the Number Guessing Game

"""  
User enter any number between the range of 1 to 20
and computer randomly also selecting the random value between 1 to 20
4 attempts will be given the user if they select the correct in 4 attempts then display congrats!! You win
otherwise you will be lose...
"""
import os
import time

def show_intro():
    os.system('cls' if os.name == 'nt' else 'clear')

    print(r"""
███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗ 
████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗
██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝

              G U E S S   T H E   N U M B E R
""")
    print("=" * 60)
    print("        I am thinking of a number... can you guess it?")
    print("=" * 60)
    time.sleep(2)

show_intro()

import random as r

count = 0

random = r.randint(1 , 20)

while count < 4 :
    guess = int(input("\nGuess the Number Between (1 - 20) : "))

    if guess not in range(1 , 21) :
        print("\nInvalid Choice Of Selection!!")
        continue

    count = count + 1 # count += 1

    if random > guess :
        print("\nGuess the Maximum Number...")

    elif random < guess :
        print("\nGuess the Minimum Number...")

    elif random == guess :
        print("\n===================================================================")
        print("\nCongrats!! You are selecting the Correct Number in",count,"attempts")
        print("\nNUMBER GUESS GAME DEVELOPER :: @ChiragShrimali")
        break

else :
    print("\n======================================================================================================================================")
    print("\nYou are lose the game because you are not choose the correct number in 4 attempts!! Better Luck Next Time!! The correct number is :",random)
# Problem #1
# Play the game Rock Papar Scissors with the computer.
# Play it three times and best of three wins. 
# If you win, print your name in color (look for a python package to do this)
# Hint - Use random number generation

import random

actions = ["rock", "paper", "scissors"]
user_count = 0 
computer_count = 0

while True:

    if user_count == 3:
        print("Best of three times. User Wins")
        break
    elif computer_count == 3:
        print("Best of three times. Computer Wins")
        break
    else:
        user_choice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissor.\n"))
        computer_choice = random.randint(0,2)

        if user_choice < 0 or user_choice >= 3:
            print("Type a Valid Number ")
            continue


        print(f"You chose {actions[user_choice]}, computer chose {actions[computer_choice]}")
            
        if user_choice == 0 and computer_choice == 2:
            user_count += 1
            print("You win")
        elif computer_choice == 0 and user_choice == 2:
            computer_count += 1
            print("You lose")
        elif computer_choice > user_choice:
            computer_count += 1
            print("You lose")
        elif user_choice > computer_choice:
            user_count += 1
            print("You win")
        else:
            print("It's a Draw")
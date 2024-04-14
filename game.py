import random

list = ["rock","paper","scissors"]

while True:
    player_choice = None
    while (player_choice := input("Your choice ").lower().strip()) not in list:
        print("Invalid, choose again")
    computer_choice = random.choice(list)
    print("Your choice is "+player_choice)
    print("Computer choice is "+computer_choice)
    if computer_choice == player_choice:
        print("Draw Game") 
    elif computer_choice == "rock" and player_choice == "scissors":
        print("You Lost")
    elif computer_choice == "scissors" and player_choice == "rock":
        print("You Won")
    elif computer_choice == "paper" and player_choice == "scissors":
        print("You Won")
    elif computer_choice == "scissors" and player_choice == "paper":
        print("You Lost")
    elif computer_choice == "paper" and player_choice == "rock":
        print("You Lost")
    else:
        print("You Won")
    proceed_game = input("Want to play Yes/No ").lower().strip()
    if proceed_game == "no":
        break
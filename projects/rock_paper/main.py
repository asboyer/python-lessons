import boyer
from random import randint

# getting player set up
name = input("What is your name: ").strip()

if name == '' or name == ' ':
    name = 'Player_1'

# constant variables
computer_score = 0
player_score = 0
choices = ['rock', 'paper', 'scissors', 'scissor', 'r', 'p', 's']

# getting valid input
while True:
    while True:
        player_choice = input("Rock, paper, or scissors? ").lower()

        if player_choice in choices:
            break
        else:
            print("Please enter a valid input!")
            continue

    if player_choice == 'r':
        player_choice = 'rock'

    elif player_choice == 'p':
        player_choice = 'paper'

    elif player_choice == 's':
        player_choice = 'scissors'

    elif player_choice == 'scissor':
        player = 'scissors'

    computer_choice = randint(1, 3)

    if computer_choice == 1:
        computer_choice = 'rock'
    if computer_choice == 2:
        computer_choice = 'paper'
    if computer_choice == 3:
        computer_choice = 'scissors'

    print("\n" + name + " choice: " + player_choice)
    print("Computer choice: " + computer_choice + "\n")


























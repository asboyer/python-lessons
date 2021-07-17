import boyer
from random import randint

# getting player set up
name = input("What is your name: ").strip()

if name == '' or name == ' ':
    name = 'Player_1'

# constant variables
computer_score = 0
player_score = 0

# TODO: implement streak

choices = ['rock', 'paper', 'scissors', 'scissor', 'r', 'p', 's']

commands = ['clear', 'quit', 'score']

# getting valid input
while True:
    while True:
        player_choice = input("Rock, paper, or scissors? ").lower()

        if player_choice in choices:
            break
        elif player_choice in commands:
            
            # TODO: write these functions
            if player_choice == 'clear':
                clear()
            if player_choice == 'quit':
                quit()
            if player_choice == 'score':
                score()

            continue
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

    player_win = False
    computer_win = False

#______________________________________________________

    # DRAW
    if player_choice == computer_choice:
        pass

    # PLAYER WINS
    elif player_choice == 'rock' and computer_choice == 'scissors':
        player_win = True
    
    elif player_choice == 'paper' and computer_choice == 'rock':
        player_win = True

    elif player_choice == 'scissors' and computer_choice == 'paper':
        player_win = True

    # COMPUTER WINS
    elif computer_choice == 'rock' and player_choice =='scissors':
        computer_win = True

    elif computer_choice == 'paper' and player_choice == 'rock':
        computer_win = True

    elif computer_choice == 'scissors' and player_choice == 'rock':
        computer_win = True

#__________________________________


    if player_win:
        print(f'{name} wins!\n')
        player_score += 1

    elif computer_win:
        print(f'{name} loses!\n')
        computer_score += 1

    else:
        print('Draw\n')

# ____________________________________

























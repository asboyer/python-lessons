from random import randint

# ideas for improvement:
"""
- adding play again [v]
- score [v]
    - high scores
- add more input options 
- always get the correct input
- simplify code w/ functions
"""

# what can we use to repeat code?
# loops
# two types of loops:
    # for loop: does something a certain amount of times
        # ex: for i in range(0, 100):
            # here (executes 100 times)
    # while loop: does something while a condition is true
        # exs:
        # while 2 + 2 == 4:
            # do this
        # name = 'andrew'
        # while name == 'andrew':
            # print('your name is andrew')
            # name = 'sam'

name = input("Enter a name: ")
if name == "":
    name = "Player 1"

playing = True # denotes if the player is 'playing' the game or not
rounds = 0 # denotes the number of times the player has played

player_score = 0
computer_score = 0

while playing:
    choice = input("Rock, paper, or scissors? ")
    if choice == "":
        choice = "r"

    # r = rock
    # p = paper
    # s = scissors

    computer_choice = randint(1, 3)

    if computer_choice == 1:
        computer_choice = "r"
    if computer_choice == 2:
        computer_choice = "p"
    if computer_choice == 3:
        computer_choice = "s"

    print(choice + " vs. " + computer_choice)
    rounds += 1
    # rounds = rounds + 1

    if computer_choice == choice:
        print("DRAW!")

    elif computer_choice == "r" and choice == "p":
        print(name + " wins!")
        player_score += 1
    
    elif computer_choice == "s" and choice == "r":
        print(name + " wins!")
        player_score += 1

    elif computer_choice == "p" and choice == "s":
        print(name + " wins!")
        player_score += 1

    elif computer_choice == "r" and choice == "s":
        print("Computer wins!")
        computer_score += 1

    elif computer_choice == "s" and choice == "p":
        print("Computer wins!")
        computer_score += 1
    
    elif computer_choice == "p" and choice == "r":
        print("Computer wins!")
        computer_score += 1

    print('\nRounds played |' + str(rounds) + '|')
    print('-------------------')
    print(name + '\'s score: ' + str(player_score))
    print('Computer score: ' + str(computer_score))
    print('-------------------')
    print('Draws: ' + str(rounds - (player_score + computer_score)) + '\n')

    answer = input('Play again? ')
    if answer == 'n':
        playing = False

print('\nRounds played: ' + str(rounds))
print('-------------------')
print(name + '\'s score: ' + str(player_score))
print('Computer score: ' + str(computer_score))
print('-------------------')
print('Draws: ' + str(rounds - (player_score + computer_score)) + '\n')
# print('Rounds played: ' + str(rounds))
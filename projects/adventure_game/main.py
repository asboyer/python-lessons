from os import path
from random import randint

playing = True

def fr(name):
    file = open(f"text/{name}.txt", "r")
    return file.read()

def choose(level, choices):
    print(fr(f'descriptions/description{level}_{choices}'))
    return input("\n" + fr(f'choices/choice{level}_{choices}'))

def check_alive(level, choices):
    death_file = f"deaths/death{str(level)}_{str(choices)}"
    if path.exists(f'text/{death_file}.txt'):
        print(fr(death_file))
        return False
    else:
        return True

def check_win(level, choices):
    win_file = f"wins/win{str(level)}_{str(choices)}"
    if path.exists(f'text/{win_file}.txt'):
        print(fr(win_file))
        return True
    else:
        return False

def play_again():
    while True:
        choice = input("Play again? ")
        if choice.startswith('y'):
            return True
        elif choice.startswith('n'):
            return False
        elif choice.startswith('maybe'):
            if randint(0, 1) == 0:
                return False
            else:
                return True
        else:
            print("Please enter a yes or no!")

while playing:
    # initialize variables
    current_choice = ""
    prev_choices = ""
    score = 0
    alive = True
    win = False
    level = 1

    while alive and not win:
        current_choice = choose(str(level), prev_choices)
        prev_choices += current_choice
        alive = check_alive(level, prev_choices)
        win = check_win(level, prev_choices)
        if alive and not win:
            score += 100
            level += 1
        if win:
            score += 1000
    if win:
        print('you win!')
    else:
        print('game over!')
    input("Press enter to continue")

from boyer import *
from art import text2art
from os import path
from random import randint

# maintenance variables
speed = 2

# read a file of highscores
# if no highscores, make new file

# game variables
highscore = 0
highlevel = 0
playing = True
played = 0

def aprint(text):
    delay_print(text, speed)

def starter(played):
    if played == 0:
        aprint(fr('starter'))
    else:
        pass

def fr(name):
    file = open(f"text/{name}.txt", "r")
    return file.read()

def intro(played):
    clear()
    starter(played)
    aprint("Welcome to...")
    print(text2art("Boyer's\nadventure\ngame"))
    input("\nPress enter to begin\n")
    clear()

def choose(level, choices):
    aprint(fr(f'descriptions/description{str(level)}_{choices}'))
    return get_num("\n" + fr(f'choices/choice{str(level)}_{choices}'), start=0, finish=1, integer=True)

def check_alive(level, choice):
    death_file = f"deaths/death{str(level)}_{str(choice)}"

    if path.exists(f'text/{death_file}.txt'):
        aprint(fr(death_file))
        return False
    else:
        return True

def check_bonus(level):
    bonus_file = f'bonus/bonus_{str(level)}'

    if path.exists(f'text/{bonus_file}.txt'):
        clear()
        aprint('bonus question!\n'.upper())

        file = open(f'text/{bonus_file}.txt', 'r')
        lines = file.readlines()
        print(lines)


def check_win(level, choice):
    win_file = f"wins/win{str(level)}_{str(choice)}"

    if path.exists(f"text/{win_file}.txt"):
        aprint(fr(win_file))
        return True
    else:
        return False

# def check_bonus(level):
#     bonus_file = f"bonus/bonus_{str(level)}"

#     file_path = f'text/{bonus_file}.txt'

#     if path.exists(file_path):
#         clear()
#         aprint("bonus question!\n".upper())

#         file = open(file_path, "r")
#         lines = file.readlines()
#         answer = input(lines[0].strip() + " ").lower().strip()
#         answers = lines[1].strip().lower().split(" ")

#         if answer in answers or answer == lines[1].strip().lower():
#             aprint(f'Correct! You recieve {lines[2]} points!')
#             clear()
#             return int(lines[2])
#         else:
#             aprint(f'Incorrect! You missed out on some bonus points!')
#             clear()
#             return 0

def credits():
    aprint(fr('credits'))

def play_again():
    while True:
        choice = input("Play again? ")
        if choice.startswith('y'):
            return True
        elif choice.startswith('n'):
            return False
        elif choice.startswith('maybe'):
            num = randint(0, 1)
            if num == 0:
                return True
            else:
                return False
        else:
            print("Please enter a yes or no!")


while playing:

    # initializing variables
    choice = ""
    choices = ""
    score = 0
    alive = True
    win = False
    level = 1
    score_break = False
    initials = ""

    intro(played)

    while alive and not win:
        check_bonus(level)
        choice = choose(level, choices)
        choices += str(choice)
        alive = check_alive(level, choices)
        win = check_win(level, choices)
        if alive and not win:
            score += 2 * level
            level += 1
        if win:
            score += 1000 * level
        if score > highscore and not score_break:
            highscore = score
            print("new high score!".upper())
            score_break = True
            if initials != "":
                print(f"You broke {initials}'s score!")

    played+=1

    if win:
        print(text2art("\nyou win!\n".upper()))
        credits()

    else:
        print(text2art("\ngame  over!\n".upper()))

    if score_break:
        initials = input("\n\nPlease enter your initials: ")

    input("Press enter to continue")

    if not play_again():
        break

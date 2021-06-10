from boyer import *
from art import text2art
from os import path

# maintenance variables
speed = 0

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

def check_win(level, choice):
    win_file = f"wins/win{str(level)}_{str(choice)}"

    if path.exists(f"text/{win_file}.txt"):
        aprint(fr(win_file))
        return True
    else:
        return False

def credits():
    aprint(fr('credits'))


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
        choice = choose(level, choices)
        choices += str(choice)
        speed = 4
        alive = check_alive(level, choices)
        win = check_win(level, choices)
        if alive and not win:
            score += 2 * level
            level += 1
        if score > highscore and not score_break:
            highscore = score
            print("new high score!".upper())
            score_break = True
            if initials != "":
                print(f"You broke {initials}'s score!")

    played+=1

    if win:
        print(text2art("\nyou win!\n".upper()))
        score += 1000 * level
        credits()

    else:
        print(text2art("\ngame over!\n".upper()))

    if score_break:
        aprint("You set a new high score!")
        initials = input("Please enter your initials: ")
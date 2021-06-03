from boyer import *
from art import text2art

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
    return get_num(fr(f'choices/choice/{str(level)}_{choices}'), start=0, finish=1, integer=True)

while playing:

    # initializing variables
    choice = ""
    choices = ""
    score = 0
    alive = True
    win = False
    level = 1

    intro(played)

    while alive and not win:
        choice = choose(level, choices)

        # description1_.txt
    

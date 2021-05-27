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
        # set the scene
        delay_print(fr('starter'), speed)
    else:
        pass
        # you know the drill, run it back

def fr(name):
    file = open(f"descriptions/{name}.txt", "r")
    return file.read()

def intro(played):
    clear()
    starter(played)
    aprint("Welcome to...")
    print(text2art("Boyer's\nadventure\ngame"))
    input("\nPress enter to begin\n")
    clear()

while playing:
    # initializing variables
    choice = ""
    choices = ""
    score = 0
    alive = True
    win = False
    level = 1

    intro(played)

    playing = False

    # choice


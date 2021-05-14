from boyer import *

def starter(played):
    if played == 0:
        # set the scene
        delay_print(fr('starter'))
    else:
        pass
        # you know the drill, run it back

def fr(name):
    file = open(f"descriptions/{name}.txt", "r")
    return file.read()

# read a file of highscores
# if no highscores, make new file
highscore = 0
playing = True
played = 0

while playing:
    # initializing variables
    score = 0
    alive = True
    win = False
    level = 0

    clear()
    starter(played)

    # choice
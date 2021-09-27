playing = True

def fr(name):
    file = open(f"text/{name}.txt", "r")
    return file.read()

def choose(level, choices):
    pass

print(fr("choices/choice1_"))

while playing:
    # initialize variables
    current_choice = ""
    prev_choices = ""
    score = 0
    alive = True
    win = False

    while alive and not win:
        pass

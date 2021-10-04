playing = True

def fr(name):
    file = open(f"text/{name}.txt", "r")
    return file.read()

def choose(level, choices):
    print(fr(f'descriptions/description{level}_{choices}'))
    return input("\n" + fr(f'choices/choice{level}_{choices}'))

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

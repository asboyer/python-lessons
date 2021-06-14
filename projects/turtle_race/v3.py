from turtle import *
from random import randint
from boyer import delay_print

# admin variables
text_speed = 0
simulation = True

play = True

intro_file = open("intro.txt")
intro_text = intro_file.read()
delay_print(intro_text, text_speed)

# a race track
startx = -140
starty = 140
track_width = 160

speed(0)
penup()
goto(startx, starty)

for i in range(16):
    write(i, align='center')
    right(90)
    forward(10)
    pendown()
    forward(track_width - 10)
    penup()
    backward(track_width)
    left(90)
    forward(20)

turtle_dict = {}

names = ["eric", "kevin", "carson", "andrew"]
colors = ["red", "blue", "green", "yellow"]
blueprint = zip(names, colors)

for name, color in blueprint:
    turtle_dict[name] = {}
    turtle_dict[name]["turtle"] = Turtle()
    turtle_dict[name]["turtle"].shape("turtle")
    turtle_dict[name]["color"] = color
    turtle_dict[name]["turtle"].color(color)
    turtle_dict[name]["steps"] = 0
    turtle_dict[name]["total_steps"] = 0
    turtle_dict[name]["wins"] = 0

x = startx - 20
y = starty - 40

def start_line(turtles, y):
    for turtle in turtles.values():
        turtle["turtle"].penup()
        turtle["turtle"].goto(x, y)
        y -= 30

def print_name(name):
    return name[0].upper() + name[1:].lower()

def clean(string):
    return string.lower().strip()

def race(turtle):
    step = randint(1, 5)
    turtle["turtle"].forward(step)
    turtle["steps"] += step

def play_again():
    while True:
        response = input('\nPlay again? ')

        if response.lower().strip().startswith('y'):
            return True
        elif response.lower().strip().startswith('n'):
            return False
        else:
            print('Please enter a yes or no!')
            continue

def get_winner():
    while True:
        guess = input("\nWho will win? ")

        if clean(guess) in names or clean(guess) in colors:
            return guess
        else:
            print('Please give a valid guess!')
            continue

while play:

    for turtle in turtle_dict.values():
        turtle['steps'] = 0

    start_line(turtle_dict, y)


    
        guess = get_winner()

    for i in range(100):
        for turtle in turtle_dict.values():
            race(turtle)

    results = []

    for name, turtle in turtle_dict.items():
        print(f"{name[0].upper() + name[1:]}: {turtle['steps']}")
        print(f"{name[0].upper() + name[1:]}: {turtle['total_steps']}")
        results.append([turtle['steps'], name])

    results.sort()
    results.reverse()

    maximum = results[0][0]
    winners = []

    for result in results:
        if result[0] == maximum:
            winners.append(result[1])
        else:
            break

    if len(winners) > 1:
        for i in range(len(winners)):
            if not winners[i] == winners[len(winners) - 1]:
                print(print_name(winners[i]), end=" and")
            else:
                print(print_name(winners[i]) + " all tie for the win!")
    else:
        print(print_name(winners[0]) + " wins!")

    winner_colors = []

    for winner in winners:
        winner_colors.append(turtle_dict[winner]["color"])
        turtle_dict[winner]["wins"] += 1

    print("\nTurtle stats:")
    for name, turtle in turtle_dict.items():
        print(f'{print_name(name)}: {turtle["wins"]} wins')
        turtle["total_steps"] += turtle["steps"]

    if guess.lower().strip() in winners or guess.lower().strip() in winner_colors:
        print("\nYou guessed the winner!")
    else:
        print("\nYou did not guess the winner!")

    play = play_again()
    
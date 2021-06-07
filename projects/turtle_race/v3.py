from turtle import *
from random import randint

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


x = startx - 20
y = starty - 40

def start_line(turtles, y):
    for turtle in turtles.values():
        turtle["turtle"].penup()
        turtle["turtle"].goto(x, y)
        y -= 30

def print_name(name):
    return name[0].upper() + name[1:].lower()

start_line(turtle_dict, y)

def race(turtle):
    step = randint(1, 5)
    turtle["turtle"].forward(step)
    turtle["steps"] += step

guess = input("Your winner: ")

for i in range(100):
    for turtle in turtle_dict.values():
        race(turtle)

results = []

for name, turtle in turtle_dict.items():
    print(f"{name[0].upper() + name[1:]}: {turtle['steps']}")
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
    for i in winners:
        if not winners[i] == winners[len(winners) - 1]:
            print(print_name(winners[i]), end=" and")
        else:
            print(print_name(winners[i]) + " all tie for the win!")
else:
    print(print_name(winners[0]) + " wins!")

if guess.lower().strip() in winners:
    print("You guessed the winner!")
else:
    print("You did not guess the winner!")
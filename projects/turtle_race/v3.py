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

start_line(turtle_dict, y)


def race(turtle):
    step = randint(1, 5)
    turtle["turtle"].forward(step)
    turtle["steps"] += step

for i in range(100):
    for turtle in turtle_dict.values():
        race(turtle)

for name, turtle in turtle_dict.items():
    print(f"{name}: {turtle['steps']}")

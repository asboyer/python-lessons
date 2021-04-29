# imports
from boyer import * # <- '*' means import everything!
from turtle import *
from random import randint

def starting_line(turtle, y):
    turtle.penup()
    turtle.goto(-160, y)

def move(turtle, total):
    step = randint(2, 6)
    turtle.forward(step)
    total += step
    return total

# general setup
speed(0)
penup()
goto(-140, 140)

# track setup (general turtle)
for step in range(21):
    write(step, align='center')
    right(90)
    forward(10) # move forward 10 pixels
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

# make turtles

turtles = []

# eric
eric = Turtle()
eric.color('red')
eric.shape('turtle')
turtles.append(eric)

# kevin
kevin = Turtle()
kevin.color('blue')
kevin.shape('turtle')
turtles.append(kevin)

# carson
carson = Turtle()
carson.color('green')
carson.shape('turtle')
turtles.append(carson)

# andrew
andrew = Turtle()
andrew.color('yellow')
andrew.shape('turtle')
turtles.append(andrew)

# move turtles to starting line
y = 100
for t in turtles:
    starting_line(t, y)
    y -= 30

e_total = 0
k_total = 0
c_total = 0
a_total = 0

for turn in range(100):
    e_total = move(turtles[0], e_total)
    k_total = move(turtles[1], k_total)
    c_total = move(turtles[2], c_total)
    a_total = move(turtles[3], a_total)

total_list = [e_total, k_total, c_total, a_total]

print(total_list)

mainloop()
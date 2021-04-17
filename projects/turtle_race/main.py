from turtle import *
from random import randint

# main setup
speed(0)
penup()
goto(-140, 140)

# track setup
for step in range(16):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

# add the racing turtles
# eric
eric = Turtle()
eric.color('red')
eric.shape('turtle')

# kevin
kevin = Turtle()
kevin.color('blue')
kevin.shape('turtle')

# carson
carson = Turtle()
carson.color('green')
carson.shape('turtle')

# elijah
elijah = Turtle()
elijah.color('yellow')
elijah.shape('turtle')

# move turtle to starting line
eric.penup()
kevin.penup()
carson.penup()
elijah.penup()
eric.goto(-160, 100)
kevin.goto(-160, 70)
carson.goto(-160, 40)
elijah.goto(-160, 10)
eric.pendown()
kevin.pendown()
carson.pendown()
elijah.pendown()

# totals
eric_total = 0

# race the turtles
for turn in range(100):
    eric_step = randint(1, 5)
    eric.forward(eric_step)
    eric_total += eric_step
    kevin.forward(randint(1, 5))
    carson.forward(randint(1, 5))
    elijah.forward(randint(1, 5))    

# interact with user
guess = input("What turtle will win?")

# keep the turtle window open
mainloop()
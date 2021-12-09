# import libraries
from turtle import *
from random import randint

# configuration
colormode(255)

# define fucntions
def random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color(red, green, blue)
    Screen().bgcolor(red, green, blue)

def randomplace():
    x = randint(-300, 300)
    y = randint(-300, 300)
    goto(x, y)

shape(None)
speed(0)
hideturtle()

while True:
    for i in range(0, 25):
        random_color()
        randomplace()
    clear()
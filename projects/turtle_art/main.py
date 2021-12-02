# import libs
from turtle import *
from random import randint

# configuration
colormode(255)
speed(0)
shape(None)

# define functions

def randcolor():
    red = randint(0, 255)
    blue = randint(0, 255)
    green = randint(0, 255)
    color(red, green, blue)
    Screen().bgcolor((red + 20) % 255, (green + 20) % 255, (blue + 20) % 255)

def randplace():
    penup()
    x = randint(-250, 250)
    y = randint(-250, 250)
    return x, y

def randdir():
    return randint(0, 360)

def drawshape():
    num = randint(1, 2)
    length=randint(10, 100)
    height=randint(10, 100)
    begin_fill()
    for i in range(num):
        forward(length)
        right(90)
        forward(height)
        right(90)
    end_fill()

while True:
    for i in range(100):
        randcolor()
        goto(randplace())
        setheading(randdir())
        drawshape()
    clear()
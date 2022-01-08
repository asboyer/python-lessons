# this is a custom module that we make
# Modules are files full of code that you can import into your programs
# this module is filled with functions that will tell the turtle to draw a shape

import turtle
def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()
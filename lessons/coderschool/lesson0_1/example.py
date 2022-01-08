# main.py:
# You can edit this code and run it right here in the browser!
# First we'll import some turtles and shapes: 
from turtle import *
from shapes import *

# Create a turtle named Tommy:
tommy = Turtle()
tommy.shape("turtle")
tommy.speed(7)

# Draw three circles:
draw_circle(tommy, "green", 50, 25, 0)
draw_circle(tommy, "blue", 50, 0, 0)
draw_circle(tommy, "yellow", 50, -25, 0)

# Write a little message:
tommy.penup()
tommy.goto(0,-50)
tommy.color("black")
tommy.write("Teach With Code!", None, "center", "16pt bold")
tommy.goto(0,-80)

# Try changing draw_circle to draw_square, draw_triangle, or draw_star

#shapes.py
# This is a custom module we've made.  
# Modules are files full of code that you can import into your programs.
# This one teaches our turtle to draw various shapes.

import turtle

def draw_circle(turtle, color, size, x, y):
  turtle.penup()
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()
  turtle.circle(size)
  turtle.end_fill()
    
def draw_triangle(turtle, color, size, x, y):
  turtle.penup()
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()
  for i in range (3):
    turtle.forward(size*3)
    turtle.left(120)
  turtle.end_fill()
  turtle.setheading(0)
    
def draw_square(turtle, color, size, x, y):
  turtle.penup()
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()
  for i in range (4):
    turtle.forward(size*2)
    turtle.left(90)
  turtle.end_fill()
  turtle.setheading(0)
  
def draw_star(turtle, color, size, x, y):
  turtle.penup()
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()
  turtle.right(144)
  for i in range(5):
    turtle.forward(size*2)
    turtle.right(144)
    turtle.forward(size*2)
  turtle.end_fill()
  turtle.setheading(0)
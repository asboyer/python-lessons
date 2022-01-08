from turtle import *
from shapes import *

# create a turtle named jeff
jeff = Turtle()
jeff.shape('turtle')
jeff.speed(0)
jeff.penup()
jeff.forward(50)

amount_of_circles = 20
x = -500
y = -500
change = 50
for i in range(amount_of_circles):
    x += change
    y += change
    draw_circle(jeff, 'green', 50, x, y)

exitonclick()
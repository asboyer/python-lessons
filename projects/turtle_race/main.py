from turtle import *

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
eric = Turtle()
eric.color('red')
eric.shape('turtle')

# keep the turtle window open
mainloop()
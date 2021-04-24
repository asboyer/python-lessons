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
kevin_total = 0
carson_total = 0
elijah_total = 0

guess = input("Who will win?")

# race the turtles
for turn in range(100):
    
    eric_step = randint(1, 5)
    eric.forward(eric_step)
    eric_total += eric_step

    kevin_step = randint(1, 5)
    kevin.forward(kevin_step)
    kevin_total += kevin_step

    carson_step = randint(1, 5)
    carson.forward(carson_step)
    carson_total += carson_step

    elijah_step = randint(1, 5)
    elijah.forward(elijah_step)
    elijah_total += elijah_step

totals = [eric_total, kevin_total, carson_total, elijah_total]

max_total = 0
max_index = 0
for i in range(len(totals)):
    if totals[i] > max_total:
        max_total = totals[i]
        max_index = i

print(f"Eric (Red): {eric_total}")
print(f"Kevin (Blue): {kevin_total}")
print(f"Carson (Green): {carson_total}")
print(f"Elijah (Yellow): {elijah_total}")

if max_index == 0:
    print('Eric Wins!')
    winner = 'eric'
elif max_index == 1:
    print('Kevin Wins!')
    winner = 'kevin'
elif max_index == 2:
    print('Carson wins!')
    winner = 'carson'
else:
    print('Elijah wins')
    winner = 'elijah'

if guess.lower().strip().startswith(winner):
    print("YOU GUESSED THE WINNER!")
else:
    print("YOU DID NOT GUESS THE WINNER!")

# keep the turtle window open
mainloop()
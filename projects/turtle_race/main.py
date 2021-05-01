from boyer import delay_print
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

# andrew
andrew = Turtle()
andrew.color('yellow')
andrew.shape('turtle')

# move turtle to starting line
eric.penup()
kevin.penup()
carson.penup()
andrew.penup()
eric.goto(-160, 100)
kevin.goto(-160, 70)
carson.goto(-160, 40)
andrew.goto(-160, 10)

# totals
eric_total = 0
kevin_total = 0
carson_total = 0
andrew_total = 0

delay_print("""Eric: the red turtle with a hot head
Kevin: the blue, calm, and collected turtle
Carson: the green trickster, some call him slimey
Andrew: the yellow turtle, AKA turtle racings' golden child
""")

guess = input("Who will win? ")

cheat = 5
if guess.lower().strip().startswith("ballerboyer"):
    cheat = 6
    guess = "andrew"

print("Ready?")
delay_print("3.... 2... 1..", 20)
print("GO!")

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

    andrew_step = randint(1, cheat)
    andrew.forward(andrew_step)
    andrew_total += andrew_step
    if andrew_total > 330:
        andrew.backward(andrew_step)

totals = [eric_total, kevin_total, carson_total, andrew_total]

max_total = 0
max_index = 0
for i in range(len(totals)):
    if totals[i] > max_total:
        max_total = totals[i]
        max_index = i

print("WOW!", end=" ")
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
    print('Andrew wins!')
    winner = 'andrew'

talk_speed = 5

if guess.lower().strip().startswith(winner):
    print("\nNO WAY, YOU GUESSED THE WINNER!")
    print(f"Special message from {winner[0].upper() + winner[1:]}:\n") 
    delay_print("\"Thanks for believing in me, pal!", talk_speed)
    delay_print(f"And always remember: I am the best racer there is. Don't get it twisted.", talk_speed)
    delay_print("I'll see ya around...\"", talk_speed)
else:
    print(f"\nSpecial message from {winner[0].upper() + winner[1:]}:\n")
    delay_print("\"I just want to give a shout out to all my doubters...especially YOU!\"", talk_speed)

# keep the turtle window open
# mainloop()

# ball game -> create an ellipse that will act as a ball

import pygame, random, threading

def randcolor():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    return (r, b, g)

screen_color = randcolor()
ball_color = randcolor()

screen_width = 800
ball_width = 200
randomness = 10

maximum_yv = 30
maximum_xv = 30

x = 200
y = 200

xvel = 11
yvel = 10

base_yv = yvel
base_xv = xvel

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_width))
pygame.display.set_caption('Bouncing Ball')
clock = pygame.time.Clock()
done = False


while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 

    screen.fill(screen_color)

    if x >= screen_width - ball_width or x <= 0: 
        xvel = -xvel
        choice = random.randint(0, 1)
        if choice == 0:
            yvel += random.randint(-randomness, randomness)
        else:
            yvel -= random.randint(-randomness, randomness)
        print(f'yvel = {yvel}')
        ball_color = randcolor()
        screen_color = randcolor()
    if y >= screen_width - ball_width or y <= 0:
        yvel = -yvel
        choice = random.randint(0, 1)
        if choice == 0:
            xvel += random.randint(-randomness, randomness)
        else:
            xvel -= random.randint(-randomness, randomness)
        print(f'xvel = {xvel}')
        ball_color = randcolor()
        screen_color = randcolor()
    if yvel > maximum_yv or yvel < -maximum_yv:
        print('CROSSED')
        yvel = base_yv
    if xvel > maximum_xv or xvel < -maximum_xv:
        xvel = base_xv
        print('CROSSED')

    pygame.draw.ellipse(screen, ball_color, [x, y, ball_width, ball_width], 0)
    x += xvel
    y += yvel

    # if x 

    pygame.display.update()
    clock.tick(60)

pygame.quit()


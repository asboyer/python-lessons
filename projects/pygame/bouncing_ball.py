import pygame, random

# defining constants

def randcolor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

x = 200
y = 200

ball_color = randcolor()
background_color = randcolor()

max_speed = 10
min_speed = -10

xv = random.randint(min_speed, max_speed)
yv = random.randint(min_speed, max_speed)

screen_width = 600
ball_width = 20

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_width))
pygame.display.set_caption('Bouncing Ball')
clock = pygame.time.Clock()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(background_color)

    if x >= screen_width - ball_width or x <= 0:
        xv = -xv
        yv = random.randint(min_speed, max_speed)
        ball_color = randcolor()
        background_color = randcolor()        
    if y >= screen_width - ball_width or y <= 0:
        yv = -yv
        xv = random.randint(min_speed, max_speed)
        ball_color = randcolor()
        background_color = randcolor()

    pygame.draw.ellipse(screen, ball_color, [x, y, ball_width, ball_width], 0)

    x += xv
    y += yv

    pygame.display.update()
    clock.tick(60)

pygame.quit()

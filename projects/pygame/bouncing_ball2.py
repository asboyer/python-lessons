import pygame, random
# defining constants

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

x = 200
y = 200

# HERE
x2 = 300
y2 = 300

ball_color = WHITE
background_color = WHITE

xv = 10
yv = 10

# HERE
xv2 = 10
yv2 = 5

done = False

screen_width = 400
ball_width = 50

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_width))
pygame.display.set_caption('Bouncing Ball')
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(background_color)

    if x >= screen_width - ball_width or x <= 0:
        xv = -xv

    if y >= screen_width - ball_width or x <= 0:
        yv = -yv

    # HERE
    if x2 >= screen_width - ball_width or x2 <= 0:
        xv2 = -xv2

    if y2 >= screen_width - ball_width or y2 <= 0:
        yv2 = -yv2


    pygame.draw.ellipse(screen, ball_color, [x, y, ball_width, ball_width], 0)

    x += xv
    y += yv

    pygame.display.update()
    clock.tick(60)

pygame.quit()

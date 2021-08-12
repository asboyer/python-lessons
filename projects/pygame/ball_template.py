import pygame
from random import randint

class Ball:
    def __init__(self):
        self.radius = 10
        self.color = WHITE
        self.x = randint(0, screen_width)
        self.y = randint(0, screen_width)
        self.xv = randint(-max_v, max_v)
        self.yv = randint(-max_v, max_v)

    def move(self):
        if self.x >= screen_width - self.radius or self.x <= 0:
            self.xv = -self.xv

        if self.y >= screen_width - self.radius or self.y <= 0:
            self.yv = -self.yv

        pygame.draw.ellipse(screen, self.color, [self.x, self.y, self.radius, self.radius], 0)


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

x = 200
y = 200

ball_color = WHITE
background_color = BLACK

xv = 10
yv = 10

max_v = 5

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

    if y >= screen_width - ball_width or y <= 0:
        yv = -yv

    pygame.draw.ellipse(screen, ball_color, [x, y, ball_width, ball_width], 0)
   
    x += xv
    y += yv

    pygame.display.update()
    clock.tick(60)

pygame.quit()

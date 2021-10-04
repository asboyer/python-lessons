import pygame
from random import randint

class Ball:
    def __init__(self, radius, color, x, y, xv, yv):
        self.radius = radius
        self.color = color
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv

    def move(self):
        if self.x >= screen_width - self.radius or self.x <= 0:
            self.xv = -self.xv

        if self.y >= screen_width - self.radius or self.y <= 0:
            self.yv = -self.yv

        self.x += self.xv
        self.y += self.yv

        pygame.draw.ellipse(screen, self.color, [self.x, self.y, self.radius, self.radius], 0)

def randcolor():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

background_color = BLACK

screen_width = 1000
ball_width = 20
ball_amount = 300

max_v = 5
min_radius = 30
max_radius = 100

ball_list = []

done = False

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_width))
pygame.display.set_caption('Bouncing Ball')
clock = pygame.time.Clock()

for i in range(ball_amount):
    ball_width = randint(min_radius, max_radius)
    ball_color = randcolor()
    ball_x = randint(0, screen_width - ball_width)
    ball_y = randint(0, screen_width - ball_width)
    ball_xv = randint(-max_v, max_v)
    ball_yv = randint(-max_v, max_v)
    ball = Ball(
                ball_width,
                ball_color, 
                ball_x,
                ball_y,
                ball_xv,
                ball_yv
                )
    ball_list.append(ball)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(background_color)

    for ball in ball_list:
        ball.move()

    pygame.display.update()
    clock.tick(60)

pygame.quit()

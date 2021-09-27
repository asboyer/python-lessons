import pygame
from random import randint, choice

# a class is something that stores variable and functions in "objects"
# without objects: life would suck
class Ball:
    # constructor      # instance fields (parameters we pass into the object)
    def __init__(self, radius, color, x, y, xv, yv):
    # __init__ = initialize
        
        # assign variables to the object
        self.radius = radius
        self.x = x
        self.y = y
        self.xv = choice([-5, 5])
        self.yv = choice([-6, 6])

        if self.x > screen_width/2 and self.y < screen_width/2:
            self.q = 1
        elif self.x < screen_width/2 and self.y < screen_width/2:
            self.q = 2
        elif self.x < screen_width/2 and self.y > screen_width/2:
            self.q = 3
        elif self.x > screen_width/2 and self.y > screen_width/2:
            self.q = 4

        if self.q == 1:
            self.color = (255, 0, 0)
        elif self.q == 2:
            self.color = (0, 255, 0)
        elif self.q == 3:
            self.color = (0, 0, 255)
        elif self.q == 4:
            self.color = (255, 255, 255)        

    def move(self):
        if self.x >= screen_width - self.radius or self.x <= 0:
            self.xv = -self.xv
        if self.y >= screen_width - self.radius or self.y <= 0:
            self.yv = - self.yv

        self.x += self.xv
        self.y += self.yv

        pygame.draw.ellipse(screen, self.color,
                            [self.x, self.y, 
                            self.radius, self.radius],
                            0)

def randcolor():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

bg_color = BLACK
screen_width = 1000

ball_amount = 100

max_v = 5
min_radius = 50
max_radius = 100

ball_list = []

done = False

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_width))
pygame.display.set_caption('Ball')
clock = pygame.time.Clock()

for i in range(ball_amount):
    ball_width = randint(min_radius, max_radius)
    ball_color = randcolor()
    ball_x = randint(ball_width, screen_width - ball_width)
    ball_y = randint(ball_width, screen_width - ball_width)

    ball_xv, ball_yv = 0, 0

    while ball_xv == 0 and ball_yv == 0:
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
    screen.fill(bg_color)
    for ball in ball_list:
        ball.move()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
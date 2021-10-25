import pygame
from random import randint
import os

# a class is something that stores variable and functions in "objects"
# without objects: life would suck
class Ball:
    # constructor      # instance fields (parameters we pass into the object)
    def __init__(self, radius, color, x, y, xv, yv, randomize, trail):
    # __init__ = initialize
        
        # assign variables to the object
        self.radius = radius
        self.x = x
        self.y = y
        self.xv = xv
        self.oxv = xv
        self.yv = yv
        self.color = color
        self.points = []
        self.randomize = randomize
        self.trail = trail
        self.wall_hits = 0

        if self.oxv < 0:
            self.oxv = self.oxv = - self.oxv

    def move(self):

        if not self.randomize:
            if self.x >= screen_width - self.radius or self.x <= 0:
                self.xv = -self.xv
                self.wall_hits += 1
                self.color = randcolor()
            if self.y >= screen_width - self.radius or self.y <= 0:
                self.yv = - self.yv    
                self.wall_hits += 1
                self.color = randcolor()
        
        if self.randomize:
            if self.x >= screen_width - self.radius:
                self.wall_hits += 1
                self.color = randcolor()
                self.xv = -self.xv
                low = int(self.xv/2)
                high = int(-self.xv/2)
                if low > high:
                    low = -low
                    high = -high
                variance = randint(low, high)
                self.xv += variance
                if self.x > max_v:
                    self.xv = self.oxv
                if self.x + self.xv >= screen_width - self.radius:
                    self.xv = -self.oxv

            if self.x <= 0:
                self.wall_hits += 1
                self.color = randcolor()
                self.xv = -self.xv
                low = int(-self.xv/2)
                high = int(self.xv/2)
                if low > high:
                    low = -low
                    high = -high
                variance = randint(low, high)
                self.xv += variance
                if self.x + self.xv <= 0:
                    self.xv = self.oxv
                if self.x > max_v:
                    self.xv = self.oxv


            if self.y >= screen_width - self.radius or self.y <= 0:
                self.yv = - self.yv  
                self.wall_hits += 1
                self.color = randcolor()

        self.points.append([self.x, self.y, self.color])

        self.x += self.xv
        self.y += self.yv

        pygame.draw.ellipse(screen, self.color,
                            [self.x, self.y, 
                            self.radius, self.radius],
                            0)
        if self.trail:
            for point in self.points:
                pygame.draw.ellipse(screen, point[2],
                                [point[0], point[1],
                                int(self.radius),
                                int(self.radius)],
                                0)
    def get_wh(self):
        return self.wall_hits

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

ball_amount = 1

max_v = 30
min_radius = 50
max_radius = 100

ball_list = []

done = False

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((screen_width, screen_width))
pygame.display.set_caption('Ball')
clock = pygame.time.Clock()

s = 'sounds'
music = pygame.mixer.music.load(os.path.join(s, 'jazz.ogg'))

def randball():
    ball_width = randint(min_radius, max_radius)
    ball_color = randcolor()
    ball_x = randint(ball_width, screen_width - ball_width)
    ball_y = randint(ball_width, screen_width - ball_width)

    ball_xv, ball_yv = randint(-max_v, max_v), randint(-max_v, max_v)

    while ball_xv == 0 or ball_yv == 0:
        ball_xv = randint(-max_v, max_v)
        ball_yv = randint(-max_v, max_v)

    ball = Ball(
                ball_width,
                ball_color,
                ball_x,
                ball_y,
                ball_xv,
                ball_yv,
                False,
                True
                )   
    return ball

def balls(ball_list):
    for i in range(ball_amount):
        ball = randball()
        ball_list.append(ball)
    return ball_list

ball_list = balls(ball_list)

pygame.mixer.music.play(-1)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(bg_color)

    for ball in ball_list:
        ball.move()
        if ball.get_wh() > 10:
            ball_list = balls([])

    pygame.display.update()
    clock.tick(60)

pygame.quit()
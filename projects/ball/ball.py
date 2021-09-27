import pygame
from random import randint
from random import choice

# a class is something that stores variables and functions in
# objects 
class Ball:
    # constructor(instance fields)
    def __init__(self, radius, color, x, y, xv, yv):
        # assigning variables to the object
        self.radius = radius
        self.color = color
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
        self.oxv = xv
        self.oyv = yv
        self.points = []

        if self.oxv < 0:
            self.oxv = -self.oxv
        
        if self.x < screen_width/2 and self.y < screen_width/2:
            self.q = 2
            self.color = (255, 255, 255)

        elif self.x < screen_width/2 and self.y > screen_width/2:
            self.q = 3
            self.color =  (0, 255, 0)

        elif self.x > screen_width/2 and self.y > screen_width/2:
            self.q = 4
            self.color = (0, 0, 255)

        elif self.x > screen_width/2 and self.y < screen_width/2:
            self.q = 1
            self.color = (255, 0, 0)
    
    def move(self):        
        #________________________________________________
        if self.x < screen_width/2 and self.y < screen_width/2:
            self.q = 2
            self.color = (255, 255, 255)

        elif self.x < screen_width/2 and self.y > screen_width/2:
            self.q = 3
            self.color =  (0, 255, 0)

        elif self.x > screen_width/2 and self.y > screen_width/2:
            self.q = 4
            self.color = (0, 0, 255)

        elif self.x > screen_width/2 and self.y < screen_width/2:
            self.q = 1
            self.color = (255, 0, 0)
        # _____________________________________________________

        if self.x >= screen_width - self.radius:
            print(f'xv before: {self.xv}')
            self.xv = -self.xv
            low = int(self.xv/2)
            high = int(-self.xv/2)
            if low > high:
                low = -low
                high = -high
            variance = randint(low, high)
            print(f'variance: {variance}')
            self.xv += variance
            if self.x + self.xv >= screen_width - self.radius:
                self.xv = -self.oxv
            print(f'xv after: {self.xv}')
            print("______________________")

        if self.x <= 0:
            print(f'xv before: {self.xv}')
            self.xv = -self.xv
            low = int(-self.xv/2)
            high = int(self.xv/2)
            if low > high:
                low = -low
                high = -high
            variance = randint(low, high)  
            print(f'variance: {variance}')
            self.xv += variance
            if self.x + self.xv <= 0:
                self.xv = self.oxv
            print(f'xv after: {self.xv}')
            print("______________________")

        if self.y >= screen_width - self.radius or self.y <= 0:
            self.yv = - self.yv

        self.points.append([self.x, self.y, self.color])
        self.x += self.xv
        self.y += self.yv


        pygame.draw.ellipse(screen, self.color,
                            [self.x, self.y, 
                            self.radius, self.radius],
                            0)

        for point in self.points:
            pygame.draw.ellipse(screen, point[2],
                                [point[0], point[1],
                                int(self.radius/4),
                                int(self.radius/4)], 
                                0)

# color format "rgb"
# (0, 0, 0)
#  r  g  b

def randcolor():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# main game variables
bg_color = BLACK
screen_width = 1400

ball_amount = 1

max_v = 100
min_radius = 50
max_radius = 200

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



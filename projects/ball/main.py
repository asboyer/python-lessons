import pygame, random

sw = 1000

xo = sw/2
yo = sw/2
xov = 5
yov = 10
ow = sw/4

def randcolor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# colors
ORANGE = (248, 142, 0)
BLACK = (0, 0, 0)
colors = []

for i in range(5):
    colors.append(randcolor())

pygame.init() # initializes pygame
screen = pygame.display.set_mode((sw, sw))
pygame.display.set_caption('ball')
clock = pygame.time.Clock()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(colors[3])

    pygame.draw.ellipse(screen, colors[0], [xo, yo, ow, ow], 0)
    pygame.draw.ellipse(screen, colors[1], [xo + ow/10, yo + ow/10, ow * 4/5, ow * 4/5], 0)
    pygame.draw.ellipse(screen, colors[2], [xo + ow/5, yo + ow/5, ow * 3/5, ow * 3/5], 0)
    pygame.draw.ellipse(screen, colors[3], [xo + 3*(ow/10), yo + 3*(ow/10), ow * 2/5, ow * 2/5], 0)
    pygame.draw.ellipse(screen, colors[4], [xo + 4*(ow/10), yo + 4*(ow/10), ow * 1/5, ow * 1/5], 0)

    if xo > sw - ow or xo <= 0:
        colors = []
        for i in range(5):
            colors.append(randcolor())
        xov = -xov

    if yo > sw - ow or yo <= 0:
        colors = []
        for i in range(5):
            colors.append(randcolor())
        yov = -yov

    xo += xov
    yo += yov

    pygame.display.update()
    clock.tick(60)

pygame.quit()
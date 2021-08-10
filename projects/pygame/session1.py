# ball game -> create an ellipse that will act as a ball

import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (172, 29, 0)
GREEN = (0, 133, 0)
BLUE = (0, 139, 225)

x = 200
y = 200

xvel = 10
yvel = 30

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Bouncing Ball')
clock = pygame.time.Clock()
done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 

    screen.fill(BLACK)

    if x >= 580 or x <= 0: 
        xvel = -xvel        
    if y >= 580 or y <= 0:
        yvel = -yvel        

    pygame.draw.ellipse(screen, WHITE, [x, y, 20, 20], 0)
    x += xvel
    y += yvel

    # if x 

    pygame.display.update()
    clock.tick(60)

pygame.quit()


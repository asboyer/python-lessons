import pygame

# defining constants

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
VIOLET = (148, 0, 211)

x = 200
y = 200

pygame.init()

screen = pygame.display.set_mode((400, 400))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


        # EVENTS:
        # ___________________
        pygame.draw.ellipse(screen, WHITE, [x, y, 20, 20], 0)
        x += 2 # make x go up by 2
        y += 3 # make y go up by 3

        #____________________
        pygame.display.update()

pygame.quit()
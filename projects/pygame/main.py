import pygame

# define constants
#        R  G  B
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (165, 21, 1)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255,192,203)

pygame.init() # start pygame

# create a display screen: 400 x 400 pixels
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption('PyGame Intro')

done = False # we're not done displaying

while not done:
    for event in pygame.event.get(): # check the events list
        if event.type == pygame.QUIT: # if the user clicks the X
            done = True # now we're done displaying

        # EVENTS:
        screen.fill(PINK)


        pygame.draw.rect(screen, RED, [100, 200, 200, 200], 10)
        pygame.draw.polygon(screen, BLUE, [[200, 100], [100, 100], [200, 200]], 0)
        pygame.draw.ellipse(screen, GREEN, [300, 10, 50, 50], 0)


        pygame.display.update()

pygame.quit()
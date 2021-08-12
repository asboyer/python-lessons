import pygame

pygame.init() # init -> initialize

width = 400

x = 0
y = 0

done = False
screen = pygame.display.set_mode((width, width))

# %Run weds2.py

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.draw.ellipse(screen, (0, 255, 0), [x, y, 20, 20], 0)
                        # screen (r,  g,    b)    x   y  w   h   g

    x += 0.01
    y += 0.01
    pygame.display.update()

pygame.quit()
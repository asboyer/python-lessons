import pygame, random

# defining constants

def randcolor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

r = 50
g = 200
b = 0
i = 20

x = 200
y = 200

ball_color = randcolor()
background_color = (r, g, b)

maximum_speed = 200

randomness = 10

# xv = random.randint(-randomness, randomness)
# yv = random.randint(-randomness, randomness)

xv = 5
yv = 10

base_xv = xv
base_yv = yv

screen_width = 600
ball_width = 20

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_width))
pygame.display.set_caption('Bouncing Ball')
clock = pygame.time.Clock()

done = False
down_r = False
down_g = False
down_b = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if r + i > 255:
        down_r = True
    elif r - i < 0:
        down_r = False


    if g + i > 255:
        down_g = True
    elif g - i < 0:
        down_g = False

    if b + i > 255:
        down_b = True
    elif b - i < 0:
        down_b = False



    background_color = (r, g, b)
    ball_color = (-(r - 255), -(g - 255), -(b - 255))
    screen.fill(background_color)

    if x >= screen_width - ball_width or x <= 0:
        xv = -xv

        # choice = random.randint(0, 1)

        # if choice == 0:
        #     yv += random.randint(-randomness, randomness)
        # else:
        #     yv -= random.randint(-randomness, randomness)

        if down_r:
            r -= i
        else:
            r += i

        if down_g:
            g -= i
        else:
            g += i

        if down_b:
            b -= i
        else:
            b += i

        print(r, g, b)
        print("________")

        # print(f'xv: {xv}')
        # print("___________")
        # ball_color = randcolor()
    if y >= screen_width - ball_width or y <= 0:
        yv = -yv

        # choice = random.randint(0, 1)

        # if choice == 0:
        #     xv += random.randint(-randomness, randomness)
        # else:
        #     xv -= random.randint(-randomness, randomness)

        if down_r:
            r -= i
        else:
            r += i

        if down_g:
            g -= i
        else:
            g += i

        if down_b:
            b -= i
        else:
            b += i

        print(r, g, b)
        print("________")

        # print(f'yv: {yv}')
        # print("___________")
        # ball_color = randcolor()

    if yv >= maximum_speed:
        yv = base_yv
    if yv < -maximum_speed:
        yv = -base_yv
    if xv >= maximum_speed:
        xv = base_xv
    if xv < -maximum_speed:
        xv = -base_xv

    pygame.draw.ellipse(screen, ball_color, [x, y, ball_width, ball_width], 0)

    x += xv
    y += yv

    pygame.display.update()
    clock.tick(60)

pygame.quit()

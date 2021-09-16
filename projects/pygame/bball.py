import pygame
from random import randint
from random import choice

# a class is something that stores variables and functions in
# objects 
class Ball:
	# constructor(instance fields)
	def __init__(self, radius, color, x, y, xv, yv):
		# assinging varibales to the object
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
			self.yv = - self.yv
		self.x += self.xv
		self.y += self.yv

		pygame.draw.ellipse(screen, self.color,
							[self.x, self.y, 
							self.radius, self.radius],
							0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# main game variables
bg_color = BLACK
screen_width = 700

done = False

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_width))
pygame.display.set_caption('Ball')
clock = pygame.time.Clock()

ball_list = []

for i in range(200):
	ball = Ball(
				70,
				choice([RED, WHITE]),
				200,
				200,
				randint(5, 20),
				randint(5, 20)
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





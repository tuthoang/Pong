"""
Created by Timmy Hoang
EK 128 Final Project
Prof Carruthers
PONG GAME
"""
import pygame
import time

pygame.init()

class Paddle():
		#initializing paddles
	def __init__(self):
		self.x=20
		self.y = height/2
		self.x2=width-self.x
		self.y2=height/2
		self.speed = 8
		self.paddlewidth =8
		self.paddleheight = 64
		self.score = 0

		#key binds
	def handle_keys(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w]:
			self.y -= self.speed
		elif keys[pygame.K_s]:
			self.y += self.speed
		if keys[pygame.K_UP]:
			self.y2-=self.speed
		if keys[pygame.K_DOWN]:
			self.y2+=self.speed
		if keys[pygame.K_ESCAPE]:
			pygame.quit()
		#increase/decrease paddle speeds
		if keys[pygame.K_g]:
			self.speed+=1
		if keys[pygame.K_h]:
			self.speed-=1
		#boundaries of the paddles
		if self.y <= 0:
			self.y = 0
		elif self.y >= height-self.paddleheight:
			self.y = height-self.paddleheight
		if self.y2<=0:
			self.y2=0
		elif self.y2>=height-self.paddleheight:
			self.y2=height-self.paddleheight
		#slowest it can go is speed of 1
		if self.speed<=0:
			self.speed=1

			#drawing the paddles to the screen
	def display(self):
		pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.paddlewidth, self.paddleheight))
		pygame.draw.rect(screen,(255,0,0),(self.x2,self.y2,self.paddlewidth,self.paddleheight))

class Ball():
	#initializing ball
	def __init__(self):
		self.size = 12
		self.x = width/2
		self.y = height/2
		self.speed_y = 4
		self.speed_x = -4

	#this is how the ball moves and how it reacts to collisions
	def movement(self):
		self.x += self.speed_x
		self.y += self.speed_y
		keys = pygame.key.get_pressed()

		if keys[pygame.K_f]:
			self.speed_x-=3
			self.speed_y+=3
                
		#wall collisions
		if self.y <= 0:
			self.speed_y *= -1
		elif self.y >= height-4:
			self.speed_y *= -1

		#paddle1 collisions
		for n in range(-self.size, paddle1.paddleheight):
			if self.y == paddle1.y + n:
				if self.x <= paddle1.x + paddle1.paddlewidth:
					self.speed_x *= -1
					break
			n += 1

		#paddle2 collisions
		for n in range(-self.size, paddle2.paddleheight):
			if self.y == paddle2.y2 + n:
				if self.x >= paddle2.x2 - paddle2.paddlewidth:
					self.speed_x *= -1
					break
			n += 1
			#draw the paddles
	def display(self):
		pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.size, self.size))

#window dimensions
width = 800
height = 600

WHITE=(255,255,255)
BLACK=(0,0,0)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('EK 128 PONG')
FPS = 60
myfont=pygame.font.SysFont("arial",15)
clock = pygame.time.Clock()
paddle1 = Paddle()
paddle2 = Paddle()
ball = Ball()


#score function
def paddle_scores( paddle, ball ):
    paddle.score += 1
    ball.__init__()
#players input their names
paddle1_input=input("Player 1 Name:")
paddle2_input=input("Player 2 Name:")

"""def winner_pad1():
	if paddle1.score==7:
		running = False
		print("winner: %s" %(paddle1_input))
		pygame.init()
		main()
		paddle1.score,paddle2.score=0,0

def winner_pad2():
	if paddle2.score==7:
		running = False
		print("winner: %s" %(paddle2_input))
		pygame.init()
		main()
		paddle1.score,paddle2.score=0,0"""
pygame.mixer.music.load('monday_converted.ogg')
pygame.mixer.music.play(1,0.0)
#game loop
def main():
	running = True
	while running:
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()

		ball.movement()
		paddle1.handle_keys()
		paddle2.handle_keys()

		screen.fill((0, 0, 0))
		ball.display()
		paddle1.display()
		paddle2.display()
		#draws the scores to the screen
		screen.blit(myfont.render("%s 's Score: %d " % (paddle1_input,paddle1.score), True, WHITE), [50, 0])
		screen.blit(myfont.render("%s 's Score: %d " % (paddle2_input,paddle2.score), True, WHITE), [500, 0])
		#scoring 
		if ball.x <=0:
			paddle_scores(paddle2,ball)
		if ball.x>width:
			paddle_scores(paddle1,ball)
		#winner_pad1()
		#winner_pad2()
		pygame.display.flip()
		clock.tick(FPS)

if __name__ == "__main__":
	main()

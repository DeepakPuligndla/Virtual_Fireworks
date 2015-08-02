#importing libraries
import pygame
import time
import threading
import math
import random 

def blast1(cx,cy,radius,thickness,angle):
	if angle < 360:
		X = int(cx + radius*6*(math.cos(angle)))
		Y = int(cy + radius*6*(math.sin(angle)))
		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)

		pygame.draw.circle(screen, (r,g,b), (X,Y), radius, thickness)
		pygame.display.update()
		blast1(cx,cy,radius,thickness, angle+30)

def blast2(cx,cy,radius,thickness,angle):
	if angle < 360:
		X = int(cx + radius*8*(math.cos(angle)))
		Y = int(cy + radius*8*(math.sin(angle)))
		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)

		pygame.draw.circle(screen, (r,g,b), (X,Y), radius, thickness)
		pygame.display.update()
		blast2(cx,cy,radius,thickness, angle+30)

def threadFunction(color,x,y,radius,thickness):
	y_axis = 0; C_y = y
	while y_axis < 300: 
		pygame.draw.circle(screen, color, (x,y), radius, thickness)
		pygame.display.update()
		time.sleep(0.0)
		pygame.draw.circle(screen, (0,0,0), (x,y), radius, thickness)
		pygame.display.update()
		y_axis += 5; y = C_y - y_axis
	blast1(x,y,radius,thickness,0)	
	blast2(x,y,radius,thickness,0)

	time.sleep(1)


pygame.init()							#initializing pygame
screen = pygame.display.set_mode((500,500))			#setting dimensions for the window to display
pygame.display.Info()						#showing window


running = True							#Variable to check the user desire to continue the program or not

while running:							#loop the executes until user clicks the close button on the window
	pygame.mixer.music.load('rocketIgnition.mp3')


	thread1 = threading.Thread(target = threadFunction, args = ((255,0,0), 150,500, 6, 2))
	thread2 = threading.Thread(target = threadFunction, args = ((0,255,0), 350,500, 6, 2))

	pygame.mixer.music.play(0)				#play the song that we loaded recent
	time.sleep(0.5)						#wait for 0.5sec


	thread1.start()
	thread2.start()

	thread1.join()
	thread2.join()

	pygame.display.update()
	screen.fill((0,0,0))
	pygame.display.update()
	
	for event in pygame.event.get():			#loop that constantly checks for user input event
		if event.type == pygame.QUIT:
			running = False

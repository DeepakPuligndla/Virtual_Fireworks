#importing libraries
import pygame
import time


pygame.init()							#initializing pygame
screen = pygame.display.set_mode((500,500))			#setting dimensions for the window to display
pygame.display.Info()						#showing window

img1 = pygame.image.load('fw1.gif')				#loading two different firework images and storing the references into two
img2 = pygame.image.load('fw2.gif')				#different variables

running = True							#Variable to check the user desire to continue the program or not

pygame.mixer.music.load('firecracker1.mp3')			#loading firecracker1.mp3 soundtrack
pygame.mixer.music.load('rocketIgnition.mp3')			#loading rocketIgnition.mp3 soundtrack

while running:							#loop the executes until user clicks the close button on the window
	pygame.display.update()					#update the screen

	crackerY1 = 0;	crackerY2 = 0				#variables to keep track of the pixels that cracker to be moved before
								#bursting	

		pygame.mixer.music.play(0)				#play the song that we loaded recent
		time.sleep(0.5)						#wait for 0.5sec

	while crackerY1 < 200 and crackerY2 < 260:		#loop that moves the cracker from ground to certain position in the window

		pygame.draw.circle(screen, (255,0,0), (150,500-crackerY1), 5, 4)
		pygame.draw.circle(screen, (0,255,0), (250,500-crackerY2), 5, 4)
		crackerY1 += 5
		crackerY2 += 6
		pygame.display.update()
		screen.fill((0,0,0))
		time.sleep(0.01)

	#loop ends once all the rockets reaches their positions

	screen.blit(img1,(150-99,300-101))			#displaying the loaded cracker images at the positions where we stopped them
	pygame.display.update()
	time.sleep(0.1)			

	screen.blit(img2,(250-99,240-101))	
	pygame.display.update()
	time.sleep(1.5)			

	for event in pygame.event.get():			#loop that constantly checks for user input event
		if event.type == pygame.QUIT:
			running = False

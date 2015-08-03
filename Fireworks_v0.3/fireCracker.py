import pygame
import threading
import time
import math
import random

class start_fireworks(object):
	threads = 0

	def __init__(self, no_of_crackers):
		self.threads = no_of_crackers
		self.initiateWindow()

	def initiateWindow(self):
		pygame.init()
		window = pygame.display.set_mode((500,500))
		pygame.display.Info()

		running = True

		while running:
				self.fire(self.threads, window)
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						running = False

	def fire(self,threads, window):
		total_threads = []

		''' (pending) generate the arguments randomly '''
		for i in range(0,threads):
			if i%2==0:
				thread = threading.Thread(target = self.moveCracker, args = ((255,0,0),  6, 2, window))
			else:
				thread = threading.Thread(target = self.moveCracker, args = ((0,255,0),  6, 2, window))
			total_threads.append(thread)
			thread.start()

		for i in range(0,threads):
			total_threads[i].join()

		window.fill((0,0,0))			
		time.sleep(2)

	def moveCracker(self,color, radius, thickness, window):
		initial_Y = 500
		initial_X = random.randint(150,350)
		end_Y = random.randint(250,350)
		y_axis = 0; temp_initial_Y = initial_Y; 
		while y_axis < end_Y: 
			pygame.draw.circle(window, color, (initial_X,initial_Y), radius, thickness)
			pygame.display.update()
			pygame.draw.circle(window, (0,0,0), (initial_X,initial_Y), radius, thickness)
			pygame.display.update()
			y_axis += 1; initial_Y = temp_initial_Y - y_axis
		self.blast1(initial_X,initial_Y,radius,thickness,0, window)	
		time.sleep(1)

	def blast1(self, cx,cy,radius,thickness,angle, window):
		if angle < 360:
			X = int(cx + radius*6*(math.cos(angle)))
			Y = int(cy + radius*6*(math.sin(angle)))
			r = random.randint(0,255)
			g = random.randint(0,255)
			b = random.randint(0,255)

			pygame.draw.circle(window, (r,g,b), (X,Y), radius, thickness)
			pygame.display.update()
			self.blast1(cx,cy,radius,thickness, angle+30, window)		
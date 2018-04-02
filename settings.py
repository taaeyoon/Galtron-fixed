import pygame as pg

class Settings():
	"""A class to store all settings for game"""
	def __init__(self):
		"""Initialize the class"""
		self.windowCaption = 'Galtron'
		#issue 113 start.
		self.screenWidth = 800	#origin450
		self.screenHeight = 700	#origin550
		#issue 113 fixed
		self.bgColor = (20, 20, 20)
		self.bg = pg.image.load("gfx/background.bmp")

		#Ships speed
		self.shipLimit = 3

		#Bullet settings
		self.bulletWidth = 3
		self.bulletHeight = 15
		self.bulletColor = (60, 60, 60)

		#Alien settings

		#How quickly the game speeds up
		self.speedUp = 1.1
		self.scoreSpeedUp = 1.5

		self.initDynamicSettings()

	def initDynamicSettings(self):
		self.shipSpeed = 0.7	#issue 119 fixed. origin1.5
		self.bulletSpeed = 3	#origin 3
		self.alienSpeed = 1		#origin 1
		self.fleetDropSpeed = 5	#origin 5
		self.fleetDir = 1
		self.alienPoints = 50

	def increaseSpeed(self):
		"""Increase the speed settings"""
		#self.shipSpeed *= self.speedUp
		#self.bulletSpeed *= self.speedUp
		if self.alienSpeed <= 1.5:
			self.alienSpeed *= self.speedUp
			self.fleetDropSpeed *= self.speedUp
		self.alienPoints = int(self.alienPoints * self.scoreSpeedUp)

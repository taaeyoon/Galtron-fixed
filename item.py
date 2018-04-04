import pygame as pg
import random
from pygame.sprite import *

class Item(Sprite):
	"""A class to manage speed item droped from the alien"""

	def __init__(self, setting, screen, pos):
		"""Create a item object at the aliens current position"""
		super(Item, self).__init__()
		self.screen = screen

		#load the item image and set its rect attribute
		self.image = pg.image.load('gfx/item_speed.png')
		self.rect = self.image.get_rect()

		#Create a collision mask
		self.mask = pg.mask.from_surface(self.image)

		#Create a items rect at (0,0)+-5
		##self.rect = pg.Rect(0, 0, setting.bulletWidth, setting.bulletHeight)
		self.rect.centerx = randint(alien.rect.centerx-5,alien.rect.centerx+5)
		self.rect.bottom = alien.rect.bottom

		#store the item position as a decimal value
		self.y = float(self.rect.y)

		self.itemSpeed = setting.bulletSpeed * 0.4


	def update(self):
		"""Move the item -y up the screen"""
		#update the decimal position of the item
		self.y += self.bulletSpeed
		#Update the rect position
		self.rect.y = self.y


	def drawitem(self):
		"""Draw the item to the screen"""
		#pg.draw.rect(self.screen, self.color, self.rect)
		self.screen.blit(self.image, self.rect)


# class ItemHeal(Sprite):
#
# 	def __init__(self, setting, screen, item):
# 		"""Create a item object at the aliens current position"""
# 		super(Item, self).__init__()
# 		self.screen = screen
#
# 		#load the item image and set its rect attribute
# 		self.image = pg.image.load('gfx/item_heal.png')
# 		self.rect = self.image.get_rect()
#
# 		#Create a collision mask
# 		self.mask = pg.mask.from_surface(self.image)
#
# 		#Create a items rect at (0,0)+-5
# 		##self.rect = pg.Rect(0, 0, setting.bulletWidth, setting.bulletHeight)
# 		self.rect.centerx = randint(alien.rect.centerx-5,alien.rect.centerx+5)
# 		self.rect.bottom = alien.rect.bottom
#
# 		#store the item position as a decimal value
# 		self.y = float(self.rect.y)
#
# 		self.itemSpeed = setting.bulletSpeed * 0.4
#
#
# 	def update(self):
# 		"""Move the item -y up the screen"""
# 		#update the decimal position of the item
# 		self.y += self.bulletSpeed
# 		#Update the rect position
# 		self.rect.y = self.y
#
#
# 	def drawitem(self):
# 		"""Draw the item to the screen"""
# 		#pg.draw.rect(self.screen, self.color, self.rect)
# 		self.screen.blit(self.image, self.rect)
#
# class ItemShield(Sprite):
#
# 	def __init__(self, setting, screen, item):
# 		"""Create a item object at the aliens current position"""
# 		super(Item, self).__init__()
# 		self.screen = screen
#
# 		#load the item image and set its rect attribute
# 		self.image = pg.image.load('gfx/item_shield.png')
# 		self.rect = self.image.get_rect()
#
# 		#Create a collision mask
# 		self.mask = pg.mask.from_surface(self.image)
#
# 		#Create a items rect at (0,0)+-5
# 		##self.rect = pg.Rect(0, 0, setting.bulletWidth, setting.bulletHeight)
# 		self.rect.centerx = randint(alien.rect.centerx-5,alien.rect.centerx+5)
# 		self.rect.bottom = alien.rect.bottom
#
# 		#store the item position as a decimal value
# 		self.y = float(self.rect.y)
#
# 		self.itemSpeed = setting.bulletSpeed * 0.4
#
#
# 	def update(self):
# 		"""Move the item -y up the screen"""
# 		#update the decimal position of the item
# 		self.y += self.bulletSpeed
# 		#Update the rect position
# 		self.rect.y = self.y
#
#
# 	def drawitem(self):
# 		"""Draw the item to the screen"""
# 		#pg.draw.rect(self.screen, self.color, self.rect)
# 		self.screen.blit(self.image, self.rect)
#
# class ItemPower(Sprite):
#
# 	def __init__(self, setting, screen, item):
# 		"""Create a item object at the aliens current position"""
# 		super(Item, self).__init__()
# 		self.screen = screen
#
# 		#load the item image and set its rect attribute
# 		self.image = pg.image.load('gfx/item_power.png')
# 		self.rect = self.image.get_rect()
#
# 		#Create a collision mask
# 		self.mask = pg.mask.from_surface(self.image)
#
# 		#Create a items rect at (0,0)+-5
# 		##self.rect = pg.Rect(0, 0, setting.bulletWidth, setting.bulletHeight)
# 		self.rect.centerx = randint(alien.rect.centerx-5,alien.rect.centerx+5)
# 		self.rect.bottom = alien.rect.bottom
#
# 		#store the item position as a decimal value
# 		self.y = float(self.rect.y)
#
# 		self.itemSpeed = setting.bulletSpeed * 0.4
#
#
# 	def update(self):
# 		"""Move the item -y up the screen"""
# 		#update the decimal position of the item
# 		self.y += self.bulletSpeed
# 		#Update the rect position
# 		self.rect.y = self.y
#
#
# 	def drawitem(self):
# 		"""Draw the item to the screen"""
# 		#pg.draw.rect(self.screen, self.color, self.rect)
# 		self.screen.blit(self.image, self.rect)

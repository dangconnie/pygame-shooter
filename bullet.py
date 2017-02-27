# Same info as hero applies here (this will be a sprite)
import pygame;

from pygame.sprite import Sprite;

from hero import Hero;

class Bullet (Sprite):
	def __init__(self, screen, hero, game_settings):
		# inheritace!
		super(Bullet, self).__init__(); 

		# Get the screen so the object can use it whenever needed
		self.screen = screen;

		# Create a bullet looking thing from scratch. starts at (0,0) goes 3 across, 10 down
		# we want bullet to originate from hero
		self.rect = pygame.Rect(0,0,game_settings.bullet_width,game_settings.bullet_height);

		# Set the centerx of the bullet we just created to the centerx of the hero
		self.rect.centerx = hero.rect.centerx;
		# Set the top to the hero top
		# self.rect.top = hero.rect.top; same as
		self.rect.centery = hero.rect.centery;

		# Set the color of the bullet from game_settings
		self.color = game_settings.bullet_color;

		# Set speed from game_settings
		self.speed = game_settings.bullet_speed;

		# Create an x and y property
		self.x = self.rect.x;
		self.y = self.rect.y;

	def update(self):
		# change the x and y accordingly based on self.speed
		# Change y in the negative every time update runs. this will subtract 20 every time update runs
		self.y -= self.speed;
		# Actually change the y coordinate of this bullet (to be self.y)
		self.rect.y = self.y;

	def draw_bullet(self):
		# draw rect takes 3 args: what entity, what color and what 
		# above, we set self.rect at (0,0)
		# draw, not blit. draw is like canvas (redrawing). blit takes an image and sets it on top of another
		pygame.draw.rect(self.screen, self.color, self.rect);
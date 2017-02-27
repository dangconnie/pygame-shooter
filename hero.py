# include pygame again. we have it b/c we pip installed it
import pygame;

# we are going to make hte hero a Sprite. Sprites are special objects in pygame that come with cool features. So we need to include the class 

from pygame.sprite import Sprite;


# Create a class called Hero. Make it a subclass of Sprite(imported above)
class Hero(Sprite):
	# Classes have two parts:
	# 1. Properties/data,
	# 2. Methods
	# Initialize the class properties with __init__. Start with just self.
	def __init__(self, image, screen):	
		# Because this is a subclass, we need to call super so that the parent clas gets the data
		super(Hero, self).__init__();
		# Give our hero an image property!
		self.image = pygame.image.load(image);
		# If your image is too big, you can resize it with the transform Methods
		self.image = pygame.transform.scale(self.image, (100, 100));

		# ..Rect stuff...
		# rect is available on all pygame entities. It's like the x and y in canvas
		self.rect = self.image.get_rect();
		# It will attach the screen to the object itself
		# Add the screen to the object so that we use and reuse it
		self.screen = screen;

		# Find out the location and size of our screen (with get_rect())
		self.screen_rect = self.screen.get_rect();

		# check screen size with print self.screen_rect;

		# So to put our hero on the left side middle, set the self.rect properties to match those of the screen accordingly
		# get vertical center of screen to self the rect of "self" (the hero)
		self.rect.centery = self.screen_rect.centery;

		# Set tje left side of the this object to the left side of the screen
		self.rect.left = self.screen_rect.left;

	def draw_me(self):
		# First arg is what, second is where (just like ReactDOM.render())
		self.screen.blit(self.image, self.rect);
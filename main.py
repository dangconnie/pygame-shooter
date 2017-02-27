# The reason you have access to pygame is becayse you ran: 
# $pip install pygame

import pygame;
# import sys so that we can halt our program. Sys is a part of core so no need to install
import sys;

# import hero class
from hero import Hero;

# get the settings class so that we can create a settings object to pass around to everyone else
from settings import Settings;

from pygame.sprite import Group, groupcollide;

# bring in bullets module
from bullet import Bullet;

# Core game functionality
def run_game():
	# initialize all the pygame stuff...
	pygame.init();
	# create a tuple got the screen_size

	# create a settings object
	game_settings = Settings();

	# screen_size = (600, 600);
	# screen_size = (game_settings.screen_size);
	# Create a screen for our game to use. We will pass this everywhere
	screen = pygame.display.set_mode(game_settings.screen_size);
	# This sets the title of the window (just like <title>)
	pygame.display.set_caption("A heroic pygame shooter")


	# Create a hero object from our hero class
	the_hero = Hero('images/hero.png', screen);

	# Make a group for the bullets to live in
	bullets = Group();
	new_bullet = Bullet(screen, the_hero, game_settings);
	bullets.add(new_bullet);

	# Make the main game loop...it will run forever...
	while 1:
		# Pygame automativally creates and event queue(like just)
		# We want to patch into certain events (like click, keypress, quit...)
		for event in pygame.event.get():
			# Check to see if the event that occurred is the quit event
			if event.type == pygame.QUIT:
				# The user clicked the red X. Stop the game. User wants off
				sys.exit();
		# Create a tuple for the background color. It's in RGB format (0 is no red, green or blue)
		# bg_color = (82, 111, 53);
		# bg_img = "images/alice_in_wonderland_bkgd.jpg";
		# Actually fill in the screen
		screen.fill(game_settings.bg_color);

		the_hero.draw_me();

		# loop through all bullets in the bullets group. call the one we're on "bullet"
		for bullet in bullets.sprites():
			bullet.update();
			bullet.draw_bullet();

		# flip the screen, i.e. wipe it out so that pygame can redraw
		pygame.display.flip();

# Run the game!
run_game();
# The reason you have access to pygame is becayse you ran: 
# $pip install pygame

import pygame;
# import sys so that we can halt our program. Sys is a part of core so no need to install
# import sys;

import time;

from game_functions import check_events, update_screen;

# import hero class
from hero import Hero;

# get the settings class so that we can create a settings object to pass around to everyone else
from settings import Settings;

from pygame.sprite import Group, groupcollide;

from enemy import Enemy;

# bring in bullets module
# from bullet import Bullet;

# Test static function
# from game_functions import utility_functions;
# utility_functions.check_events();

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

	# to make hero group 
	the_hero_group = Group();
	the_hero_group.add(the_hero);

	# Make a group for the bullets to live in
	bullets = Group();
	# we only want to add a bullet in check_events
	# new_bullet = Bullet(screen, the_hero, game_settings);
	# bullets.add(new_bullet);

	enemies = Group();
	# on a certain time, we want to add a new enemy

	game_start_time = time.time();
	print game_start_time;

	# Make the main game loop...it will run forever...
	while 1:
		# Create a tuple for the background color. It's in RGB format (0 is no red, green or blue)
		# bg_color = (82, 111, 53);
		# bg_img = "images/alice_in_wonderland_bkgd.jpg";
		# Actually fill in the screen
		screen.fill(game_settings.bg_color);

		# time between unix time stamp and when we started the game
		game_settings.timer = (time.time() - game_start_time);
		# print game_settings.timer;
		# let's print number of seconds that have passed
		# print int(game_settings.timer);

		if int(game_settings.timer) % 5 == 0:
			# add new enemy to group after a certain time
			enemies.add(Enemy(screen, game_settings));

		# line below calls game_functions module
		check_events(screen, the_hero, game_settings, bullets, enemies);

		update_screen(screen, the_hero, game_settings, bullets, enemies);


# Run the game!
run_game();
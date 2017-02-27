import pygame;
# import sys so that we can halt our program. Sys is a part of core so no need to install
import sys;

# bring in bullets module
from bullet import Bullet;

# class utility_functions(object): 
# 	# @staticmethod
# 	def check_events():
# 		print "static test";


# we need access to screen, hero and game_settings
def check_events(screen, hero, game_settings, bullets, enemies):
	# Pygame automativally creates and event queue(like just)
	# We want to patch into certain events (like click, keypress, quit...)
	for event in pygame.event.get():
		# Check to see if the event that occurred is the quit event
		if event.type == pygame.QUIT:
			# The user clicked the red X. Stop the game. User wants off
			sys.exit();
		# The user presses a key...	
		elif event.type == pygame.KEYDOWN:	
			# What key was pressed?
			if event.key == pygame.K_SPACE:
				new_bullet = Bullet(screen, hero, game_settings, 'up', 'vertical');
				bullets.add(new_bullet);
			# print event.key;
			elif event.key == pygame.K_a:
				new_bullet = Bullet(screen, hero, game_settings, 'right', 'horizontal');
				bullets.add(new_bullet);

def update_screen(screen, the_hero, game_settings, bullets, enemies):
	the_hero.draw_me();
	# loop through all bullets in the bullets group. call the one we're on "bullet"
	for bullet in bullets.sprites():
		bullet.update();
		bullet.draw_bullet();
	for enemy in enemies:
		enemy.update_me(the_hero);
		enemy.draw_me();
	# flip the screen, i.e. wipe it out so that pygame can redraw
	pygame.display.flip();
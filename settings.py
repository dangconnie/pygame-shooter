# A place to keep all our settings so that they are easy to change later

class Settings():
	def __init__(self):
		self.screen_size = (600, 600);
		self.bg_color = (82, 111, 53);
		self.bullet_width = 3;
		self.bullet_height = 10;
		self.bullet_color = (0,0,0);
		self.bullet_speed = 5;
		self.timer = 0;

		self.game_active = False;

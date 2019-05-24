# Author: Tianyao (Till) Chen
# Email: tillchen417@gmail.com
# File: settings.py

class Settings:
    """The class to store all the settings for Alien Invasion."""
    def __init__(self):
        """Initialize the settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Ship settings
        self.ship_speed = 6
        self.ship_limit = 3
        # Bullet settings.
        self.bullet_speed = 10.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # Alien settings.
        self.alien_speed = 3.0
        self.fleet_drop_speed = 15
        self.fleet_direction = 1 # 1 means right, -1 means left


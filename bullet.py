# Author: Tianyao (Till) Chen
# Email: tillchen417@gmail.com
# File: bullet.py

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """The class to manage the bullets shot from the ship."""
    def __init__(self, game):
        """Initialize the bullet."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color
        # Create a bullet rectangle at (0,0) first and then set the correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = game.ship.rect.midtop
        # Store the position.
        self.y = float(self.rect.y)

    def update(self):
        """The class to update the position of the bullet."""
        self.y -= self.settings.bullet_speed # for float value
        self.rect.y = self.y # for rectangle
    
    def draw_bullet(self):
        """Draw the bullet."""
        pygame.draw.rect(self.screen, self.color, self.rect)
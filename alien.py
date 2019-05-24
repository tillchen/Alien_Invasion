# Author: Tianyao (Till) Chen
# Email: tillchen417@gmail.com
# File: alien.py

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """The class that manages the aliens."""
    def __init__(self, game):
        """Inialize an alien and set the position."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        # Load the image and set it to rectangular.
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        # Add the alien from the top left corner.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store the position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if aline is at the edge."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left < 0:
            return True

    def update(self):
        """Move the alien horizontally"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
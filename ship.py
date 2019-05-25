# Author: Tianyao (Till) Chen
# Email: tillchen417@gmail.com
# File: ship.py

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """The class to manage the ship."""
    def __init__(self, game):
        """Initialize the ship and put it to the default position."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()
        # Load the image and set it to rectangle.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        # Start the new ship at midbottom.
        self.rect.midbottom = self.screen_rect.midbottom
        # Store the location.
        self.x = float(self.rect.x)
        # Movement flags.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at the current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
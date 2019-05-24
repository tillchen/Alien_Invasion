# Author: Tianyao (Till) Chen
# Email: tillchen417@gmail.com
# File: button.py

import pygame.font

class Button:
    """The class that manages the start button."""
    def __init__(self, game, msg):
        """Initialize the button attributes."""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        # Set the properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        # Build the rectangle object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        # Button message.
        self._prep_msg(msg)

    def _prep_msg(self, msg): # helper method
        """Prepare the message and change it to an image centered in the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        """Draw the button and the message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
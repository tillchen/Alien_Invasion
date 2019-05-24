# Author: Tianyao (Till) Chen
# Email: tillchen417@gmail.com
# File: scoreboard.py

import pygame.font

class Scoreboard:
    """The class that reports scoring info."""
    def __init__(self, game):
        """Initialize the scoreboard attributes."""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats
        # Font settings.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # Prepare the score image
        self.prep_score()

    def prep_score(self):
        """Render the score to an image."""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        # Put the score image at the top right corner.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def draw_score(self):
        """Draw the score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)


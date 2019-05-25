# Author: Tianyao (Till) Chen
# Email: tillchen417@gmail.com
# File: game_stats.py

class GameStats:
    """The class that tracks statistics for the game."""
    def __init__(self, game):
        """Initialize the statistics."""
        self.settings = game.settings
        self.reset_stats()
        # Start the game in an inactive state.
        self.game_active = False
        # Try to see if there's a high score record.
        try:
            with open("high_score.txt") as file_obj:
                self.high_score = int(file_obj.read())
        except FileNotFoundError:
            self.high_score = 0

    def reset_stats(self):
        """Intialize the statistics that might change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
# Author: Tianyao (Till) Chen
# Email: tillchen417@gmail.com
# File: game_stats.py

class GameStats:
    """The class that tracks statistics for the game."""
    def __init__(self, game):
        """Initialize the statistics."""
        self.settings = game.settings
        self.reset_stats()
        # Start the game in an active state.
        self.game_active = True

    def reset_stats(self):
        """Intialize the statistics that might change during the game."""
        self.ships_left = self.settings.ship_limit
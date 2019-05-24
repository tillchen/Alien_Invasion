# Author: Tianyao (Till) Chen
# Email: tillchen417@gmail.com
# File: alien_invasion.py

import sys
from time import sleep

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button

class AlienInvasion:
    """The overall class that manages the game."""
    def __init__(self):
        """Initialize the game."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # fullscreen mode
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion!")
        # Create statistics.
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        # Create the play button
        self.play_button = Button(self, "Play")

    def _create_alien(self, i, row): # helper method
        """Create an alien and put it in the row. i is the index for an alien. row i the row number"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * i
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row
        self.aliens.add(alien) 

    def _create_fleet(self): #helper method
        """Create a fleet of aliens."""
        # Create an alien
        alien = Alien(self)
        # Find the number of aliens in a row
        alien_width, alien_height = alien.rect.size
        available_x_space = self.settings.screen_width - (2 * alien_width) # full width - margins
        x_aliens = available_x_space // (2 * alien_width)
        # Find the number of rows
        ship_height = self.ship.rect.height
        available_y_space = self.settings.screen_height - (3 * alien_height) - ship_height # full height - margin - ship height
        y_aliens = available_y_space // (2 * alien_height)
        # Create the fleet
        for row in range(y_aliens):
            for i in range(x_aliens):
                self._create_alien(i, row)

    def _fire_bullet(self): # helper method
        """Create a bullet and add it to the group."""
        if len(self.bullets) < self.settings.bullets_allowed: # limit the number of bullets
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_keydown(self, event): # helper method
        """Check for pressing keys."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True # set the flag to true
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True # set the flag to true
        elif event.key == pygame.K_q: # press q to quit
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup(self, event): # helper method
        """Check for releasing keys."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False # set the flag to false
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False # set the flag to false

    def _check_play_button(self, mouse_pos): # helper method
        """Start the game when the button is clicked."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active: # not respond to clicks when the game is active
            # Reset the statistics.
            self.stats.reset_stats()
            self.stats.game_active = True
            # Purge aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()
            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()
            # Hide the cursor
            pygame.mouse.set_visible(False)

    def _check_events(self): # helper method, private with one leading underscore
        """Watch for keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _update_screen(self): # helper method
        """Update images and flip to the new screen."""
        self.screen.fill(self.settings.bg_color) # redraw the screen for each iteration.
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # Draw the button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip() # make the most recently drawn screen visible

    def _check_bullet_alien_collisions(self): # helper method
        """Chekc for bullet-alien collisions."""
        # Check for bullet-alien collision
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        # If all aliens are destroyed, generate a new fleet
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _update_bullets(self): # helper method
        """Update the positions of bullets and delete old bullets."""
        self.bullets.update() # update the positions
        # Deleting the old bullets.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0: # if reach the top, y = 0
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _ship_hit(self): # helper method
        """Respond to ship being hit by an alien."""
        if self.stats.ships_left > 1:
            self.stats.ships_left -= 1
            # Purge aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()
            # Create a new fleet and re-center the ship.
            self._create_fleet()
            self.ship.center_ship()
            # Pause.
            sleep(1.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_aliens(self): # helper method
        """Update the postions of the aliens."""
        self._check_fleet_edges()
        self.aliens.update()
        # Check for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        # Check for aliens that reach the bottom
        self._check_aliens_bottom()

    def _change_fleet_direction(self): # helper method
        """Change the fleet direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_fleet_edges(self): # helper method
        """Change the fleet direction if an alien hits the edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _check_aliens_bottom(self):
        """Chekc if any alien reaches the bottom, then reduce one ship."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            if self.stats.game_active: 
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

if __name__ == "__main__":
    # Create a game instance and run it
    game = AlienInvasion()
    game.run_game()
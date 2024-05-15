import pygame
from constants import ENEMY_IMAGE, ENEMY_SPEED, SCREEN_HEIGHT, IMAGE_SIZE

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """Initialize the enemy sprite, setting up the image and initial position."""
        super().__init__()
        self.image = self.load_and_transform_image()
        self.rect = self.image.get_rect(center=(x, y))

    def load_and_transform_image(self):
        """Load the enemy image, rotate, and scale it."""
        original_image = pygame.image.load(ENEMY_IMAGE).convert_alpha()
        rotated_image = pygame.transform.rotate(original_image, 45)
        return pygame.transform.scale(rotated_image, IMAGE_SIZE)

    def update(self):
        """Update the enemy's position and check for screen boundary crossing."""
        self.move()
        self.check_boundaries()

    def move(self):
        """Move the enemy downward based on the defined speed."""
        self.rect.move_ip(0, ENEMY_SPEED)

    def check_boundaries(self):
        """Remove the enemy from the game if it crosses the bottom screen boundary."""
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

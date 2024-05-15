import pygame
from constants import BULLET_IMAGE, IMAGE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, dx, dy):
        """Initialize the bullet sprite with position and direction."""
        super().__init__()
        self.image = self.load_scaled_image()
        self.rect = self.image.get_rect(center=(x, y))
        self.dx = dx
        self.dy = dy

    def load_scaled_image(self):
        """Load and scale the bullet image from the specified path."""
        original_image = pygame.image.load(BULLET_IMAGE).convert_alpha()
        return pygame.transform.scale(original_image, IMAGE_SIZE)

    def update(self):
        """Update the bullet's position and handle boundary crossing."""
        self.move()
        self.check_boundaries()

    def move(self):
        """Move the bullet according to its velocity."""
        self.rect.move_ip(self.dx, self.dy)

    def check_boundaries(self):
        """Remove the bullet from the game if it crosses the screen boundaries."""
        if (self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT or
            self.rect.left < 0 or self.rect.right > SCREEN_WIDTH):
            self.kill()

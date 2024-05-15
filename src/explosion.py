import pygame
from constants import EXPLOSIONS_PATH

class Explosion(pygame.sprite.Sprite):
    # Class variable to store explosion frames to avoid reloading images for every explosion
    frames = []

    def __init__(self, center):
        """Initialize the explosion at the specified center position."""
        super().__init__()
        if not Explosion.frames:
            Explosion.load_frames()
        self.current_frame = 0
        self.image = Explosion.frames[self.current_frame]
        self.rect = self.image.get_rect(center=center)
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50  # milliseconds

    @classmethod
    def load_frames(cls):
        """Load all frames at once and scale them; called once per game or level init."""
        if not cls.frames:  # Load only if not already loaded
            for i in range(13):
                img_path = f'{EXPLOSIONS_PATH}/tile00{i+1}.png'
                img = pygame.image.load(img_path).convert_alpha()
                img = pygame.transform.scale(img, (100, 100))  # Scale to desired size
                cls.frames.append(img)

    def update(self):
        """Update the animation frame of the explosion."""
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.current_frame += 1
            if self.current_frame == len(Explosion.frames):
                self.kill()  # Remove the sprite after the last frame
            else:
                self.image = Explosion.frames[self.current_frame]
                self.rect = self.image.get_rect(center=self.rect.center)

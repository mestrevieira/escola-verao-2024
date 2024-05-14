import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.images = []
        for i in range(13): 
            img = pygame.image.load(f'images/explosions/tile00{i+1}.png').convert_alpha()
            img = pygame.transform.scale(img, (100, 100))  # Scale to desired size
            self.images.append(img)
        self.current_frame = 0
        self.image = self.images[self.current_frame]
        self.rect = self.image.get_rect(center=center)
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50  # milliseconds

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.current_frame += 1
            if self.current_frame == len(self.images):
                self.kill()  # Remove the sprite after the last frame
            else:
                self.image = self.images[self.current_frame]
                self.rect = self.image.get_rect(center=self.rect.center)

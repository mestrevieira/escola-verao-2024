import pygame
from constants import *

# Bullet class  
class Bullet(pygame.sprite.Sprite):  
    def __init__(self, x, y, dx, dy):  
        super().__init__()  
        original_image = pygame.image.load('images/bullet.png').convert_alpha()
        self.image = pygame.transform.scale(original_image, IMAGE_SIZE) 
        self.rect = self.image.get_rect(center=(x, y))  
        self.dx = dx  
        self.dy = dy  
      
    def update(self):  
        self.rect.move_ip(self.dx, self.dy)  
        if self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT or self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:  
            self.kill()  
  
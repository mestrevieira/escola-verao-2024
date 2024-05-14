import pygame
from constants import *

# Enemy class  
class Enemy(pygame.sprite.Sprite):  
    def __init__(self, x, y):  
        super().__init__()  
        original_image = pygame.image.load('images/enemy.png').convert_alpha() 
        original_image = pygame.transform.rotate(original_image, 45)
        self.image = pygame.transform.scale(original_image, IMAGE_SIZE)
        self.rect = self.image.get_rect(center=(x, y))   
      
    def update(self):  
        self.rect.move_ip(0, ENEMY_SPEED)  
        if self.rect.top > SCREEN_HEIGHT:  
            self.kill()  
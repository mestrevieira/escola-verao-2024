import pygame
from constants import *

# Player class  
class Player(pygame.sprite.Sprite):  
    def __init__(self):  
        super().__init__()  
        original_image = pygame.image.load('images/player.png').convert_alpha() 
        self.image = pygame.transform.scale(original_image, IMAGE_SIZE) 
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))  
  
    def update(self, pressed_keys):  
        if pressed_keys[pygame.K_LEFT]:  
            self.rect.move_ip(-PLAYER_SPEED, 0)  
        if pressed_keys[pygame.K_RIGHT]:  
            self.rect.move_ip(PLAYER_SPEED, 0)  
        if pressed_keys[pygame.K_UP]:  
            self.rect.move_ip(0, -PLAYER_SPEED)  
        if pressed_keys[pygame.K_DOWN]:  
            self.rect.move_ip(0, PLAYER_SPEED)  
          
        # Keep player on the screen  
        if self.rect.left < 0:  
            self.rect.left = 0  
        if self.rect.right > SCREEN_WIDTH:  
            self.rect.right = SCREEN_WIDTH  
        if self.rect.top < 0:  
            self.rect.top = 0  
        if self.rect.bottom > SCREEN_HEIGHT:  
            self.rect.bottom = SCREEN_HEIGHT  
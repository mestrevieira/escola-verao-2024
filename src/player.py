import pygame
from constants import *

class Player(pygame.sprite.Sprite):  
    def __init__(self):  
        super().__init__()  
        original_image = pygame.image.load(PLAYER_IMAGE).convert_alpha() 
        self.image = pygame.transform.scale(original_image, IMAGE_SIZE) 
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))  
        self.score = 0
      
    def update_score(self, inc=10):
        self.score += inc
    
    def update(self, pressed_keys):  
        if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:  
            self.rect.move_ip(-PLAYER_SPEED, 0)  
        if pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:  
            self.rect.move_ip(PLAYER_SPEED, 0)  
        if pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]:  
            self.rect.move_ip(0, -PLAYER_SPEED)  
        if pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]:  
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
import random

# Constants  
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 1024
IMAGE_SIZE = (60, 60) 
PLAYER_SIZE = 50  
ENEMY_SIZE = 50  
BULLET_SIZE = 5  
WHITE = (255, 255, 255)  
RED = (255, 0, 0)  
GREEN = (0, 255, 0)  
BLUE = (0, 0, 255)  
PLAYER_SPEED = 5  
BULLET_SPEED = 10  
ENEMY_SPEED = 2  
DIAGONAL_BULLET_SPEED = (BULLET_SPEED // (2 ** 0.5), BULLET_SPEED // (2 ** 0.5))  # Adjust for diagonal movement  

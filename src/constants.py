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
TEXT_FONT = 'assets/font/VeniteAdoremus-rgRBA.ttf'

# IMAGES
BULLET_IMAGE = 'assets/images/bullet.png'
ENEMY_IMAGE = 'assets/images/enemy.png'
PLAYER_IMAGE = 'assets/images/player.png'
EXPLOSIONS_PATH = 'assets/images/explosions'
GAMEOVER_IMAGE = 'assets/images/background_game_over.png'
WELCOME_IMAGE = 'assets/images/background_welcome.png'
BACKGROUND_IMAGE = 'assets/images/background.png'

# SOUNDS
EXPLOSION_SOUND = 'assets/sounds/explosion.mp3'
OPENING_THEME = 'assets/sounds/opening_theme.mp3'
BACKGROUND_MUSIC = 'assets/sounds/music.mp3'
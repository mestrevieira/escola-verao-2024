from enum import Enum
import random

# Screen dimensions
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 1024

# Asset sizes
IMAGE_SIZE = (50, 50)
PLAYER_SIZE = 50
ENEMY_SIZE = 50
BULLET_SIZE = 5

# Colors defined using an Enum for better readability
class Color(Enum):
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

# Movement speeds
PLAYER_SPEED = 5
ENEMY_SPEED = 5
BULLET_SPEED = 15
ROOT_TWO = 1.414  # Square root of 2, used for diagonal speed calculation
DIAGONAL_BULLET_SPEED = (BULLET_SPEED / ROOT_TWO, BULLET_SPEED / ROOT_TWO)

# Font paths
TEXT_FONT = 'assets/font/VeniteAdoremus-rgRBA.ttf'

# Image paths
BULLET_IMAGE = 'assets/images/bullet.png'
ENEMY_IMAGE = 'assets/images/enemy.png'
PLAYER_IMAGE = 'assets/images/player.png'
EXPLOSIONS_PATH = 'assets/images/explosions'
GAMEOVER_IMAGE = 'assets/images/background_game_over.png'
WELCOME_IMAGE = 'assets/images/background_welcome.png'
BACKGROUND_IMAGE = 'assets/images/background.png'

# Sound paths
EXPLOSION_SOUND = 'assets/sounds/explosion.mp3'
OPENING_THEME = 'assets/sounds/opening_theme.mp3'
BACKGROUND_MUSIC = 'assets/sounds/music.mp3'

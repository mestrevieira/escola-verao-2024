import pygame
from welcome_screen import WelcomeScreen
from game import Game
from game_over import GameOver
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    pygame.init()
    welcome_screen = WelcomeScreen(pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)))
    welcome_screen.run()
    game = Game()
    game.run()
    game_over = GameOver(pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)))
    game_over.run()
    pygame.quit()


if __name__ == "__main__":
    main()
import pygame
from welcome_screen import WelcomeScreen
from game import Game
from game_over import GameOver

def run_game():
    """Setup and run the main game loop."""
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Invasão Cibernética na Escola de Verão")
    welcome_screen()
    run_game()
    game_over_screen()
    
def welcome_screen():
    """Run the welcome screen"""
    welcome_screen = WelcomeScreen()
    welcome_screen.run()

def run_game():
    """Run the main game"""
    game = Game()
    game.run()

def game_over_screen():
    """Run the game over screen"""
    game_over = GameOver()
    game_over.run()

if __name__ == "__main__":
    run_game()
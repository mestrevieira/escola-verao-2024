import pygame
import sys
from constants import *

class GameOver:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        pygame.display.set_caption("Invasão Cibernética na Escola de Verão")
        self.background = pygame.image.load(GAMEOVER_IMAGE).convert()
        self.font = pygame.font.Font(TEXT_FONT, 30)
        self.text = self.font.render('Game Over', True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(self.screen_width / 2, self.screen_height / 2))
        self.show_text = True
        self.last_switch = pygame.time.get_ticks()
        self.switch_interval = 1000  # milliseconds
        
    def run(self):
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            # Stop the music when the game starts
                            pygame.mixer.music.stop()
                            running = False  # Exit the welcome screen and return to the game

                self.screen.blit(self.background, (0, 0))
                current_time = pygame.time.get_ticks()
                if current_time - self.last_switch > self.switch_interval:
                    self.show_text = not self.show_text
                    self.last_switch = current_time

                if self.show_text:
                    self.screen.blit(self.text, self.text_rect)

                pygame.display.flip()


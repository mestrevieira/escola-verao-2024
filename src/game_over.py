import pygame
import sys
from constants import GAMEOVER_IMAGE, TEXT_FONT, SCREEN_WIDTH, SCREEN_HEIGHT

class GameOver:
    def __init__(self):
        """Initialize the game over screen with all necessary components."""
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Invasão Cibernética na Escola de Verão")
        self.setup_background()
        self.setup_text()

    def setup_background(self):
        """Load and set the background image for the game over screen."""
        self.background = pygame.image.load(GAMEOVER_IMAGE).convert()

    def setup_text(self):
        """Prepare the 'Game Over' text and its properties."""
        font = pygame.font.Font(TEXT_FONT, 30)
        self.text = font.render('Perdeste!', True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(self.screen.get_width() / 2, self.screen.get_height() / 2))

    def run(self):
        """Run the game over screen loop."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return True  # Signal to exit the game over screen

            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.text, self.text_rect)
            pygame.display.flip()
        return False  # This return statement may be used to indicate the game should not continue

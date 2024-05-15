import pygame
import sys
from audiomanager import AudioManager
from constants import WELCOME_IMAGE, TEXT_FONT, SCREEN_WIDTH, SCREEN_HEIGHT

class WelcomeScreen:
    def __init__(self):
        """Initialize the welcome screen with all necessary components."""
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        pygame.display.set_caption("Invasão Cibernética na Escola de Verão")
        self.setup_background()
        self.setup_text()
        self.setup_audio()

    def setup_background(self):
        """Load and set the background image for the welcome screen."""
        self.background = pygame.image.load(WELCOME_IMAGE).convert()

    def setup_text(self):
        """Prepare the 'Press Start' text and its properties."""
        font = pygame.font.Font(TEXT_FONT, 30)
        self.text = font.render('Carrega no Enter!', True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(self.screen_width / 2, self.screen_height / 2))
        self.show_text = True
        self.last_switch = pygame.time.get_ticks()
        self.switch_interval = 500  # milliseconds

    def setup_audio(self):
        """Initialize and play opening music for the welcome screen."""
        self.audio_manager = AudioManager()
        self.audio_manager.play_music('opening')

    def run(self):
        """Run the welcome screen loop."""
        running = True
        while running:
            running = not self.handle_events()  # Exit loop if handle_events signals to stop
            self.update_screen()

    def handle_events(self):
        """Handle events within the welcome screen."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key is pygame.K_RETURN:
                pygame.mixer.music.stop()  # Stop the music
                return True  # Signal to stop the running loop
        return False  # Continue running

    def update_screen(self):
        """Update the screen content and handle text blinking."""
        self.screen.blit(self.background, (0, 0))
        if self.should_blink_text():
            self.screen.blit(self.text, self.text_rect)
        pygame.display.flip()

    def should_blink_text(self):
        """Determine whether to show or hide the text based on the timing."""
        current_time = pygame.time.get_ticks()
        if current_time - self.last_switch > self.switch_interval:
            self.show_text = not self.show_text
            self.last_switch = current_time
        return self.show_text

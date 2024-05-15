import pygame
from pygame.locals import *
import random
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_SPEED, BACKGROUND_IMAGE, TEXT_FONT, Color
from audiomanager import AudioManager
from player import Player
from bullet import Bullet
from enemy import Enemy
from explosion import Explosion

class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.setup_screen()
        self.clock = pygame.time.Clock()
        self.running = True
        self.setup_audio()
        self.load_assets()
        self.setup_entities()
        self.setup_timing()

    def setup_screen(self):
        """Initialize the game screen and set its title."""
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Invasão Cibernética na Escola de Verão")

    def setup_audio(self):
        """Setup and start background music."""
        self.audio_manager = AudioManager()
        self.audio_manager.play_sound('music')

    def load_assets(self):
        """Load background images and set repeating patterns."""
        self.background = pygame.image.load(BACKGROUND_IMAGE).convert()
        self.background_rect = self.background.get_rect()

    def setup_entities(self):
        """Initialize all game entities and sprite groups."""
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)

    def setup_timing(self):
        """Setup timing and intervals for enemy spawns."""
        self.enemy_spawn_time = 0
        self.spawn_interval = 500

    def run(self):
        """Main game loop handling events, updates, and rendering."""
        while self.running:
            self.handle_events()
            self.update_game_logic()
            self.render()
            self.clock.tick(60)

    def handle_events(self):
        """Handle all events from the user and system."""
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN and event.key == K_SPACE or event.type == MOUSEBUTTONDOWN:
                self.shoot_bullets(self.player.rect.center)

    def update_game_logic(self):
        """Update all game logic including spawns and movements."""
        self.update_spawns()
        self.player.update(pygame.key.get_pressed())
        self.bullets.update()
        self.enemies.update()
        self.explosions.update()
        self.handle_collisions()

    def update_spawns(self):
        """Check and handle the timing for enemy spawns."""
        now = pygame.time.get_ticks()
        if now - self.enemy_spawn_time > self.spawn_interval:
            self.spawn_enemy()
            self.enemy_spawn_time = now

    def render(self):
        """Render all game components to the screen."""
        self.render_background()
        self.all_sprites.draw(self.screen)
        self.render_score()
        pygame.display.flip()

    def render_background(self):
        """Render scrolling background."""
        y_offset = (pygame.time.get_ticks() // 10) % self.background_rect.height
        self.screen.blit(self.background, (0, y_offset - self.background_rect.height))
        self.screen.blit(self.background, (0, y_offset))

    def render_score(self):
        """Render player's score on the screen."""
        font = pygame.font.Font(TEXT_FONT, 36)
        score_text = font.render(f"SCORE: {self.player.score}", True, Color.WHITE.value)
        score_text_rect = score_text.get_rect(center=(SCREEN_WIDTH - 150, 50))
        self.screen.blit(score_text, score_text_rect)

    def shoot_bullets(self, position):
        """Create a bullet and add it to the relevant groups."""
        bullet = Bullet(position[0], position[1], 0, -BULLET_SPEED)
        self.all_sprites.add(bullet)
        self.bullets.add(bullet)

    def spawn_enemy(self):
        """Spawn an enemy at a random position along the top of the screen."""
        x_position = random.randint(0, SCREEN_WIDTH)
        enemy = Enemy(x_position, 0)
        self.all_sprites.add(enemy)
        self.enemies.add(enemy)

    def handle_collisions(self):
        """Handle collisions between enemies, bullets, and the player."""
        for enemy in self.enemies:
            if pygame.sprite.spritecollide(enemy, self.bullets, True):
                enemy.kill()
                self.audio_manager.play_sound('explosion')
                explosion = Explosion(enemy.rect.center)
                self.all_sprites.add(explosion)
                self.explosions.add(explosion)
                self.player.update_score(10)

            if pygame.sprite.collide_rect(self.player, enemy):
                self.end_game()

    def end_game(self):
        """Handle end-game scenario including stopping music and finalizing gameplay."""
        self.player.kill()
        explosion = Explosion(self.player.rect.center)
        self.all_sprites.add(explosion)
        self.explosions.add(explosion)
        self.audio_manager.play_sound('explosion')
        pygame.mixer.music.stop()
        self.running = False

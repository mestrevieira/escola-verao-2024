import pygame
from pygame.locals import *
import random
from audiomanager import AudioManager
from player import Player
from bullet import Bullet
from enemy import Enemy
from explosion import Explosion
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_SPEED

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Invasão Cibernética na Escola de Verão")
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.audio_manager = AudioManager()
        self.audio_manager.play_sound('music')
        
        # Load background
        self.background = pygame.image.load("images/background.png").convert()
        self.background_rect = self.background.get_rect()
        
        # Game entities
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        
        # Timing for enemy spawn
        self.enemy_spawn_time = 0
        self.spawn_interval = 500

    def run(self):
        while self.running:
            self.handle_events()
            self.update_game_logic()
            self.render()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN and event.key == K_SPACE:
                self.shoot_bullets(self.player.rect.center)

    def update_game_logic(self):
        now = pygame.time.get_ticks()
        if now - self.enemy_spawn_time > self.spawn_interval:
            self.spawn_enemy()
            self.enemy_spawn_time = now

        self.player.update(pygame.key.get_pressed())
        self.bullets.update()
        self.enemies.update()
        self.explosions.update()
        self.handle_collisions()

    def render(self):
        y_offset = (pygame.time.get_ticks() // 10) % self.background_rect.height
        self.screen.blit(self.background, (0, y_offset - self.background_rect.height))
        self.screen.blit(self.background, (0, y_offset))
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def shoot_bullets(self, position):
        bullet = Bullet(position[0], position[1], 0, -BULLET_SPEED)
        self.all_sprites.add(bullet)
        self.bullets.add(bullet)

    def spawn_enemy(self):
        x_position = random.randint(0, SCREEN_WIDTH)
        enemy = Enemy(x_position, 0)
        self.all_sprites.add(enemy)
        self.enemies.add(enemy)

    def handle_collisions(self):
        for enemy in self.enemies:
            if pygame.sprite.spritecollide(enemy, self.bullets, True):
                enemy.kill()
                self.audio_manager.play_sound('explosion')
                explosion = Explosion(enemy.rect.center)
                self.all_sprites.add(explosion)
                self.explosions.add(explosion)

            if pygame.sprite.collide_rect(self.player, enemy):
                self.end_game()

    def end_game(self):
        self.player.kill()
        explosion = Explosion(self.player.rect.center)
        self.all_sprites.add(explosion)
        self.explosions.add(explosion)
        self.audio_manager.play_sound('explosion')
        pygame.mixer.music.stop()
        self.running = False
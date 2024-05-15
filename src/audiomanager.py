import pygame 
from constants import * 

class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {
            'explosion': pygame.mixer.Sound(EXPLOSION_SOUND),
            'music': BACKGROUND_MUSIC,
            'opening': OPENING_THEME
        }

    def play_sound(self, name):
        if name in self.sounds:
            if name == 'music' or name == 'opening':
                pygame.mixer.music.load(self.sounds[name])
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play(loops=-1)
            else:
                self.sounds[name].play()

    def stop_music(self):
        pygame.mixer.music.stop()
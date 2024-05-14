import pygame 

class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {
            'explosion': pygame.mixer.Sound('sound/explosion.mp3'),
            'music': 'sound/music.mp3'
        }
        self.sounds['explosion'].set_volume(0.5)

    def play_sound(self, name):
        if name in self.sounds:
            if name == 'music':
                pygame.mixer.music.load(self.sounds['music'])
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play(loops=-1)
            else:
                self.sounds[name].play()

    def stop_music(self):
        pygame.mixer.music.stop()
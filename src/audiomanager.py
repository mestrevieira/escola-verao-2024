import pygame
from constants import EXPLOSION_SOUND, BACKGROUND_MUSIC, OPENING_THEME

class AudioManager:
    def __init__(self):
        """Initialize the audio manager and load necessary sound files."""
        pygame.mixer.init()
        self.load_sounds()

    def load_sounds(self):
        """Load sounds and handle potential loading errors."""
        try:
            self.sounds = {
                'explosion': pygame.mixer.Sound(EXPLOSION_SOUND),
            }
            self.music_tracks = {
                'background': BACKGROUND_MUSIC,
                'opening': OPENING_THEME,
            }
        except pygame.error as e:
            print(f"Error loading sound files: {e}")
            raise SystemExit(e)

    def play_sound(self, name):
        """Play a specific sound effect."""
        if name in self.sounds:
            self.sounds[name].play()

    def play_music(self, track_name, loops=-1, volume=0.5):
        """Play music tracks with adjustable looping and volume."""
        if track_name in self.music_tracks:
            pygame.mixer.music.load(self.music_tracks[track_name])
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play(loops=loops)

    def stop_music(self):
        """Stop any currently playing music."""
        pygame.mixer.music.stop()

    def set_volume(self, volume):
        """Set the volume for the music."""
        pygame.mixer.music.set_volume(volume)

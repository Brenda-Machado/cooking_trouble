"""
Cooking Trouble.

Gerenciador Singleton centralizado de sons e música.

sound_manager.py
"""

import pygame
import os
from typing import Dict

class SoundManager:
    _instance = None
    _sound_cache: Dict[str, pygame.mixer.Sound] = {}
    _music_cache: Dict[str, str] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            pygame.mixer.init()

        return cls._instance

    def __init__(self):
        self._asset_path = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'sounds')
        self._volume = 1.0
        self._music_volume = 0.7

    def get_sound(self, sound_name: str) -> Optional[pygame.mixer.Sound]:
        if sound_name in self._sound_cache:
            return self._sound_cache[sound_name]

        file_path = os.path.join(self._asset_path, f"{sound_name}.wav")

        try:
            sound = pygame.mixer.Sound(file_path)
            sound.set_volume(self._volume)
            self._sound_cache[sound_name] = sound

            return sound
        
        except pygame.error as e:
            print(f"Erro ao carregar som {file_path}: {e}")

            return None

    def play_sound(self, sound_name: str, loops: int = 0):
        sound = self.get_sound(sound_name)

        if sound:
            sound.play(loops)

    def set_volume(self, volume: float):
        self._volume = max(0.0, min(1.0, volume))

        for sound in self._sound_cache.values():
            sound.set_volume(self._volume)

    def load_music(self, music_name: str):
        file_path = os.path.join(self._asset_path, f"{music_name}.mp3")

        try:
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.set_volume(self._music_volume)

        except pygame.error as e:
            print(f"Erro ao carregar música {file_path}: {e}")

    def play_music(self, loops: int = -1):
        pygame.mixer.music.play(loops)

    def stop_music(self):
        pygame.mixer.music.stop()

    def clear_cache(self):
        self._sound_cache.clear()

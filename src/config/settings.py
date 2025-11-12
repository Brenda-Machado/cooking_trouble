"""
Cooking Trouble.

Configurações da aplicação.

settings.py
"""

from src.utils.constants import *
class GameSettings:
    def __init__(self):
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
        self.fps = FPS
        self.debug_mode = False
        self.volume = 1.0
        self.current_difficulty = DifficultyLevel.MEDIUM

    def toggle_debug(self):
        self.debug_mode = not self.debug_mode

    def set_volume(self, volume: float):
        self.volume = max(0.0, min(1.0, volume))

    def set_difficulty(self, difficulty: int):
        if difficulty not in [DifficultyLevel.EASY, DifficultyLevel.MEDIUM, DifficultyLevel.HARD]:
            raise ValueError("Dificuldade inválida")
        
        self.current_difficulty = difficulty
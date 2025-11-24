"""
Cooking Trouble.

Controlador principal do jogo.

game_controller.py
"""

from src.models.phase import Phase
from src.utils.coordinate import Coordinate
from src.utils.constants import GameState, DifficultyLevel
from src.services.sound_manager import SoundManager
from src.controllers.input_controller import InputController

class GameController:

    def __init__(self, phase: Phase):
        self._phase = phase
        self._input_controller = InputController()
        self._sound_manager = SoundManager()
        self._game_state = GameState.GAMEPLAY
        self._game_paused = False
        self._timer = 0
        self._max_time = 300 

    @property
    def phase(self) -> Phase:
        return self._phase

    @property
    def game_paused(self) -> bool:
        return self._game_paused

    @property
    def timer_seconds(self) -> int:
        return int(self._timer / 60) 

    @property
    def is_victory(self) -> bool:
        return self._phase.is_victory

    @property
    def is_defeat(self) -> bool:
        return self._timer >= self._max_time * 60

    def update(self, delta_time: float):
        if self._game_paused:
            return

        self._timer += 1

        if not self._input_controller.update():
            return 

        actions = self._input_controller.get_action_input()

        if actions['pause']:
            self._game_paused = True
            return

        movement = self._input_controller.get_movement_input()

        self._phase.update(movement, actions['interact'], delta_time)

    def toggle_pause(self):
        self._game_paused = not self._game_paused

    def reset(self):
        self._timer = 0
        self._game_paused = False

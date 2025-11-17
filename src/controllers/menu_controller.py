"""
Cooking Trouble.

Controlador dos menus.

menu_controller.py
"""

from src.utils.constants import GameState
from src.controllers.input_controller import InputController

class MenuController:
    def __init__(self):
        self._input_controller = InputController()
        self._current_menu_state = GameState.MAIN_MENU
        self._selected_option = 0

    @property
    def current_menu_state(self) -> str:
        return self._current_menu_state

    @property
    def selected_option(self) -> int:
        return self._selected_option

    def update(self):
        if not self._input_controller.update():
            return False

        actions = self._input_controller.get_action_input()

        if actions['pause'] or actions['back']:
            self._go_back()

        if actions['confirm']:
            self._confirm_selection()

        movement = self._input_controller.get_movement_input()

        if movement['w']:
            self._selected_option -= 1
        elif movement['s']:
            self._selected_option += 1

        return True

    def set_menu_state(self, state: str):
        self._current_menu_state = state
        self._selected_option = 0

    def _go_back(self):
        if self._current_menu_state == GameState.MAIN_MENU:
            pass 
        elif self._current_menu_state in [
            GameState.DIFFICULTY_MENU, GameState.TUTORIAL, GameState.CREDITS]:
            self._current_menu_state = GameState.MAIN_MENU
        elif self._current_menu_state in [GameState.VICTORY, GameState.DEFEAT]:
            self._current_menu_state = GameState.MAIN_MENU

    def _confirm_selection(self):
        pass

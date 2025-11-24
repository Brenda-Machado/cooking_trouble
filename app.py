"""
Cooking Trouble.

Arquivo de execução do jogo.

app.py
"""

import pygame
import sys
from src.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, GameState
from src.config.settings import GameSettings
from src.controllers.menu_controller import MenuController
from src.controllers.game_controller import GameController
from src.controllers.input_controller import InputController
from src.services.level_builder import LevelBuilder
from src.views.renderer import GameRenderer
from src.views.ui.main_menu import MainMenu

class CookingTroubleGame:
    def __init__(self):
        pygame.init()
        self._settings = GameSettings()
        self._display = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT)
        )
        pygame.display.set_caption("Cooking Trouble")

        self._clock = pygame.time.Clock()
        self._running = True
        self._game_state = GameState.MAIN_MENU
        self._menu_controller = MenuController()
        self._game_controller = None
        self._game_renderer = GameRenderer((SCREEN_WIDTH, SCREEN_HEIGHT))
        self._main_menu = MainMenu((SCREEN_WIDTH, SCREEN_HEIGHT))
        self._level_builder = LevelBuilder()

    def run(self):
        while self._running:
            self._update()
            self._render()
            self._clock.tick(FPS)

        pygame.quit()
        sys.exit()

    def _update(self):
        if self._game_state == GameState.MAIN_MENU:
            self._update_main_menu()
        elif self._game_state == GameState.GAMEPLAY:
            self._update_gameplay()

    def _render(self):
        self._display.fill((0, 0, 0))

        if self._game_state == GameState.MAIN_MENU:
            self._main_menu.render(self._display)
        elif self._game_state == GameState.GAMEPLAY:
            self._render_gameplay()

        pygame.display.flip()

    def _update_main_menu(self):
        if not self._menu_controller.update():
            self._running = False
            return

        action = self._menu_controller._input_controller.get_action_input()
        movement = self._menu_controller._input_controller.get_movement_input()

        if movement['w']:
            self._main_menu.move_cursor_up()
        elif movement['s']:
            self._main_menu.move_cursor_down()

        if action['confirm']:
            self._handle_menu_selection()

    def _handle_menu_selection(self):
        selected = self._main_menu.selected_option

        if selected == MainMenu.OPTION_PLAY:
            self._start_game()
        elif selected == MainMenu.OPTION_TUTORIAL:
            print("Tutorial não implementado")
        elif selected == MainMenu.OPTION_CREDITS:
            print("Créditos não implementado")
        elif selected == MainMenu.OPTION_EXIT:
            self._running = False

    def _start_game(self):
        level_name = "level_1"
        difficulty = self._settings.current_difficulty
        phase = self._level_builder.build_phase(level_name, difficulty)

        self._game_controller = GameController(phase)
        self._game_state = GameState.GAMEPLAY

    def _update_gameplay(self):
        self._game_controller.update(1.0 / FPS)

        if self._game_controller.is_victory:
            print("Vitória!")

            self._game_state = GameState.MAIN_MENU
            self._main_menu = MainMenu((SCREEN_WIDTH, SCREEN_HEIGHT))

        elif self._game_controller.is_defeat:
            print("Derrota!")

            self._game_state = GameState.MAIN_MENU
            self._main_menu = MainMenu((SCREEN_WIDTH, SCREEN_HEIGHT))

        if self._game_controller.game_paused:
            print("Jogo pausado... retornando ao menu")

            self._game_state = GameState.MAIN_MENU
            self._main_menu = MainMenu((SCREEN_WIDTH, SCREEN_HEIGHT))

    def _render_gameplay(self):
        phase = self._game_controller.phase
        camera_offset = phase.get_camera_position()
        timer_seconds = self._game_controller.timer_seconds

        self._game_renderer.render_phase(
            self._display, phase, camera_offset, timer_seconds
        )


def main():
    game = CookingTroubleGame()
    game.run()


if __name__ == "__main__":
    main()

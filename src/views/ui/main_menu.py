"""
Cooking Trouble.

Classe do menu principal.

main_menu.py
"""

import pygame
from src.views.ui.base_menu import BaseMenu
from src.utils.constants import COLOR_WHITE, COLOR_BLACK

class MainMenu(BaseMenu):
    OPTION_PLAY = 0
    OPTION_TUTORIAL = 1
    OPTION_CREDITS = 2
    OPTION_EXIT = 3

    def __init__(self, screen_size: tuple):
        super().__init__(screen_size)
        self._selected_option = self.OPTION_PLAY
        self._cursor_x = self._width / 2 - 150

    @property
    def selected_option(self) -> int:
        return self._selected_option

    def set_selected_option(self, option: int):
        max_option = self.OPTION_EXIT
        self._selected_option = max(0, min(option, max_option))

    def move_cursor_up(self):
        self.set_selected_option(self._selected_option - 1)

    def move_cursor_down(self):
        self.set_selected_option(self._selected_option + 1)

    def render(self, display: pygame.Surface):
        display.blit(self._background, (0, 0))

        self._draw_bordered_text(
            display, "Cozinhando em Apuros", 60,
            self._width / 2, self._height / 8,
            COLOR_WHITE, COLOR_BLACK
        )

        options = ["Jogar", "Tutorial", "Créditos", "Sair"]
        option_y = [
            self._height / 2 - 120,
            self._height / 2 - 60,
            self._height / 2,
            self._height / 2 + 60
        ]

        for i, (option, y) in enumerate(zip(options, option_y)):
            self._draw_text(display, option, 30, self._width / 2, y)

        cursor_y = option_y[self._selected_option]
        self._draw_text(display, "▶", 20, self._cursor_x, cursor_y)

        self._draw_bordered_text(
            display, "W/S: Mover | Enter: Selecionar | ESC: Voltar", 16,
            self._width / 2, self._height - 40,
            COLOR_WHITE, COLOR_BLACK
        )

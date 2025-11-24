"""
Cooking Trouble.

Classe base para os menus.

base_menu.py
"""

import pygame
from abc import ABC, abstractmethod
from src.services.image_manager import ImageManager
from src.utils.constants import COLOR_WHITE, COLOR_BLACK

class BaseMenu(ABC):
    def __init__(self, screen_size: tuple):
        self._width, self._height = screen_size
        self._font_path = 'PressStart2P-vaV7.ttf'
        self._background = self._load_background()
        self._white = COLOR_WHITE
        self._black = COLOR_BLACK

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    def _load_background(self) -> pygame.Surface:
        image_manager = ImageManager()

        return image_manager.get_background('menu_background', self._width, self._height)

    @abstractmethod
    def render(self, display: pygame.Surface):
        pass

    def _draw_text(self, display: pygame.Surface, text: str, size: int,
                   x: float, y: float, color: tuple = None):

        if color is None:
            color = self._white

        font = pygame.font.Font(self._font_path, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        display.blit(text_surface, text_rect)

    def _draw_bordered_text(self, display: pygame.Surface, text: str,
                            size: int, x: float, y: float,
                            text_color: tuple = None, border_color: tuple = None):
        if text_color is None:
            text_color = self._white
        if border_color is None:
            border_color = self._black

        font = pygame.font.Font(self._font_path, size)
        text_surface = font.render(text, True, text_color)
        border_surface = font.render(text, True, border_color)
        text_rect = text_surface.get_rect(center=(x, y))

        for offset in [(-2, -2), (-2, 2), (2, -2), (2, 2)]:
            display.blit(border_surface, text_rect.move(*offset))

        display.blit(text_surface, text_rect)

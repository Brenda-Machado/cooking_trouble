"""
Cooking Trouble.

Classes base para entidades do jogo.

entity.py
"""

import pygame
from abc import ABC, abstractmethod
from src.utils.coordinate import Coordinate
from src.utils.size import Size

class Entity(ABC):
    def __init__(self, coord: Coordinate, size: Size):
        self._coord = Coordinate(coord.x, coord.y)
        self._size = size
        self._rect = pygame.Rect(
            int(self._coord.x),
            int(self._coord.y),
            int(size.width),
            int(size.height)
        )
        self._rect.center = (int(self._coord.x), int(self._coord.y))

    @property
    def coord(self) -> Coordinate:
        return self._coord

    @coord.setter
    def coord(self, value: Coordinate):
        self._coord = Coordinate(value.x, value.y)
        self._update_rect_position()

    @property
    def size(self) -> Size:
        return self._size

    @property
    def rect(self) -> pygame.Rect:
        return self._rect

    def _update_rect_position(self):
        self._rect.center = (int(self._coord.x), int(self._coord.y))

    @abstractmethod
    def update(self, delta_time: float):
        pass

    @abstractmethod
    def draw(self, camera_offset: Coordinate) -> tuple:
        pass

    def collides_with(self, other: 'Entity') -> bool:
        return self._rect.colliderect(other.rect)

    def distance_to(self, other: 'Entity') -> float:
        return self._coord.distance_to(other.coord)

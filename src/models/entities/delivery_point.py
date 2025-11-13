"""
Cooking Trouble.

Classe que representa o ponto de entrega dos itens.

delivery_point.py
"""

import pygame
from src.models.entities.base.entity import Entity
from src.utils.coordinate import Coordinate
from src.utils.size import Size
from src.utils.constants import COLOR_GREEN_DARK

class DeliveryPoint(Entity):
    def __init__(self, coord: Coordinate, interaction_radius: float = 120):
        size = Size(120, 120)
        super().__init__(coord, size)
        self._interaction_radius = interaction_radius

    @property
    def interaction_radius(self) -> float:
        return self._interaction_radius

    def update(self, delta_time: float):
        pass

    def draw(self, camera_offset: Coordinate) -> tuple:
        rect_camera = self._rect.move(
            -int(camera_offset.x),
            -int(camera_offset.y)
        )

        surface = pygame.Surface((self._rect.width, self._rect.height))
        surface.set_alpha(100)
        surface.fill(COLOR_GREEN_DARK)

        return surface, rect_camera

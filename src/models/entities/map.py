"""
Cooking Trouble.

Classe do mapa do jogo.

map.py
"""

import pygame
import random
from src.utils.coordinate import Coordinate
from src.utils.size import Size
from src.services.image_manager import ImageManager
from src.models.entities.base.entity import Entity
from typing import List, Tuple

class GameMap(Entity):
    def __init__(self, map_name: str, width: int = 1280, height: int = 720):
        super().__init__(Coordinate(0, 0), Size(width, height))
        self._map_name = map_name
        self._width = width
        self._height = height
        self._obstacles: List[pygame.Rect] = []
        self._spawn_points: List[Coordinate] = []
        self._delivery_points: List[Coordinate] = []
        self._item_spawns: List[Coordinate] = []
        self._background = self._load_background()

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @property
    def obstacles(self) -> List[pygame.Rect]:
        return self._obstacles

    def add_obstacle(self, x: int, y: int, width: int, height: int):
        rect = pygame.Rect(x, y, width, height)
        self._obstacles.append(rect)

    def get_obstacle_rects(self) -> List[pygame.Rect]:
        return self._obstacles

    def get_random_item_spawn(self) -> Coordinate:
        if self._item_spawns:
            
            return random.choice(self._item_spawns).copy()
        return Coordinate(self._width / 2, self._height / 2)

    def _load_background(self) -> pygame.Surface:
        image_manager = ImageManager()

        return image_manager.get_background(self._map_name, self._width, self._height)

    def update(self, delta_time: float):
        pass

    def draw(self, camera_offset: Coordinate) -> Tuple[pygame.Surface, pygame.Rect]:
        rect_camera = self._rect.move(
            -int(camera_offset.x),
            -int(camera_offset.y)
        )

        return self._background, rect_camera

    def get_render_data(self, camera_offset: Coordinate) -> List[Tuple]:
        data = []
        image, rect = self.draw(camera_offset)

        if image and rect:
            data.append((image, rect))

        return data

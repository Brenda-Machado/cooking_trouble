"""
Cooking Trouble.

Classe que representa os itens coletáveis.

item.py
"""

import pygame
from src.models.entities.base.entity import Entity
from src.utils.coordinate import Coordinate
from src.utils.size import Size
from src.services.image_manager import ImageManager

class Item(Entity):
    def __init__(self, coord: Coordinate, item_type: str, interaction_radius: float = 120):
        size = Size(60, 60) 
        super().__init__(coord, size)
        self._item_type = item_type
        self._interaction_radius = interaction_radius
        self._is_active = True
        self._image = self._load_image()

    @property
    def item_type(self) -> str:
        return self._item_type

    @property
    def interaction_radius(self) -> float:
        return self._interaction_radius

    @property
    def is_active(self) -> bool:
        return self._is_active

    def activate(self):
        self._is_active = True

    def deactivate(self):
        self._is_active = False

    def _load_image(self):
        image_manager = ImageManager()
        
        return image_manager.get_sprite(
            'item', self._item_type,
            self._size.width,
            self._size.height
        )

    def update(self, delta_time: float):
        pass

    def draw(self, camera_offset: Coordinate) -> tuple:
        if not self._is_active:
            return None, None

        rect_camera = self._rect.move(
            -int(camera_offset.x),
            -int(camera_offset.y)
        )
        
        return self._image, rect_camera


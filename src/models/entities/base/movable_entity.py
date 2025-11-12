"""
Cooking Trouble.

Classe base para entidades que se movem.

movable_entity.py
"""

import pygame
from abc import abstractmethod
from src.models.entities.base.entity import Entity
from src.utils.coordinate import Coordinate
from src.utils.size import Size

class MovableEntity(Entity):
    def __init__(self, coord: Coordinate, size: Size, speed: float):
        super().__init__(coord, size)
        self._speed = speed
        self._direction = Coordinate(0, 0)
        self._angle = 0
        self._knockback_time = 0
        self._knockback_source = None
        self._images = []
        self._current_image_index = 0

    @property
    def speed(self) -> float:
        return self._speed

    @speed.setter
    def speed(self, value: float):
        if value < 0:
            raise ValueError("Velocidade não pode ser negativa")
        
        self._speed = value

    @property
    def direction(self) -> Coordinate:
        return self._direction

    @direction.setter
    def direction(self, value: Coordinate):
        self._direction = Coordinate(value.x, value.y)
        self._angle = Coordinate.calculate_angle(value.x, value.y)
        self._update_rect_rotation()

    @property
    def angle(self) -> int:
        return self._angle

    @property
    def is_knockbacked(self) -> bool:
        return self._knockback_time > 0

    @property
    def knockback_time_remaining(self) -> int:
        return self._knockback_time

    @property
    def images(self) -> list:
        return self._images

    def apply_knockback(self, source_coord: Coordinate, duration: int):
        self._knockback_time = duration
        self._knockback_source = Coordinate(source_coord.x, source_coord.y)
        direction = Coordinate.unit_vector(source_coord, self._coord)
        self._direction = direction

    def get_effective_speed(self) -> float:
        if self.is_knockbacked:
            return self._speed * 2
        
        return self._speed

    def _update_rect_rotation(self):
        if not (self._angle >= 315 or self._angle <= 45 or 
                (self._angle >= 135 and self._angle <= 225)):
            self._rect.width = int(self._size.height)
            self._rect.height = int(self._size.width)

        else:
            self._rect.width = int(self._size.width)
            self._rect.height = int(self._size.height)

    def update(self, delta_time: float):
        if self.is_knockbacked:
            self._knockback_time -= 1

        speed = self.get_effective_speed()
        displacement = Coordinate(
            self._direction.x * speed,
            self._direction.y * speed
        )

        self._coord.move(displacement.x, displacement.y)
        self._update_rect_position()

    @abstractmethod
    def decide_direction(self):
        pass

    @abstractmethod
    def on_collision(self, other_coord: Coordinate):
        pass

    @abstractmethod
    def load_images(self, sprite_names: list) -> list:
        pass

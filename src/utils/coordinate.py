"""
Cooking Trouble.

Classe para gerenciar coordenadas bidimensionais.

coordinates.py
"""

from typing import Tuple
from math import sqrt

class Coordinate:
    def __init__(self, x: float, y: float):

        self._x = float(x)
        self._y = float(y)

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value: float):
        self._x = float(value)

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value: float):
        self._y = float(value)

    def move(self, dx: float, dy: float) -> 'Coordinate':
        self._x += dx
        self._y += dy

        return self

    def distance_to(self, other: 'Coordinate') -> float:
        dx = self._x - other.x
        dy = self._y - other.y

        return sqrt(dx * dx + dy * dy)

    @staticmethod
    def unit_vector(from_coord: 'Coordinate', to_coord: 'Coordinate') -> 'Coordinate':
        dx = to_coord.x - from_coord.x
        dy = to_coord.y - from_coord.y

        distance = sqrt(dx * dx + dy * dy)

        if distance == 0:
            return Coordinate(0, 0)

        return Coordinate(dx / distance, dy / distance)

    @staticmethod
    def calculate_angle(dx: float, dy: float) -> int:
        if dx != 0 and dy != 0:
            if abs(dx) >= 0.924:
                return 270 if dx > 0 else 90
            elif abs(dy) >= 0.924:
                return 180 if dy > 0 else 0
            else:
                if dx > 0:
                    return 225 if dy > 0 else 315
                else:
                    return 135 if dy > 0 else 45
        return 0

    def copy(self) -> 'Coordinate':
        return Coordinate(self._x, self._y)

    def __repr__(self) -> str:
        return f"Coordinate({self._x}, {self._y})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Coordinate):
            return False
        
        return self._x == other.x and self._y == other.y

    def __hash__(self) -> int:
        return hash((self._x, self._y))

    def as_tuple(self) -> Tuple[float, float]:
        return (self._x, self._y)

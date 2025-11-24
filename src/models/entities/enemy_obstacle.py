"""
Cooking Trouble.

Inimigo obstáculo móvel.

enemy_obstacle.py
"""

from typing import List
from src.models.entities.base.movable_entity import MovableEntity
from src.utils.coordinate import Coordinate
from src.utils.size import Size
from src.services.image_manager import ImageManager

class EnemyObstacle(MovableEntity):
    def __init__(self, path: List[Coordinate], speed: float = 2.0):
        if not path:
            raise ValueError("Caminho não pode estar vazio")

        super().__init__(path, Size(55, 55), speed)
        self._path = [Coordinate(p.x, p.y) for p in path]
        self._path_index = 0
        self._images = self.load_images([
            'idle_up', 'idle_down', 'walk_left_1', 'walk_left_2',
            'walk_right_1', 'walk_right_2', 'hurt_up', 'hurt_down'
        ])
        self._current_image = self._images

    @property
    def path(self) -> List[Coordinate]:
        return self._path

    @property
    def current_path_index(self) -> int:
        return self._path_index

    def decide_direction(self):
        if self.is_knockbacked:
            return

        if self._path_index >= len(self._path):
            self.direction = Coordinate(0, 0)
            return

        target = self._path[self._path_index]
        distance = self._coord.distance_to(target)

        if distance < 10: 
            self._path_index = (self._path_index + 1) % len(self._path)

            if self._path_index < len(self._path):
                target = self._path[self._path_index]

        self.direction = Coordinate.unit_vector(self._coord, target)

    def on_collision(self, other_coord: Coordinate):
        self.apply_knockback(other_coord, 30)

    def load_images(self, sprite_names: List[str]) -> List:
        image_manager = ImageManager()
        images = []

        for name in sprite_names:
            img = image_manager.get_sprite(
                'enemy_obstacle', name,
                int(self._size.width),
                int(self._size.height)
            )
            images.append(img)
            
        return images

    def get_current_image(self):
        if self.is_knockbacked:
            return self._images[6 if self._angle < 180 else 7]

        if self._direction.x == 0 and self._direction.y == 0:
            return self._images[0 if self._angle < 180 else 1]

        if self._direction.x < 0 or (self._direction.x == 0 and self._direction.y < 0):
            if self._current_image == self._images:
                return self._images
            
            return self._images

        if self._current_image == self._images:
            return self._images
        
        return self._images

    def draw(self, camera_offset: Coordinate) -> tuple:
        self._current_image = self.get_current_image()
        rect_camera = self._rect.move(-int(camera_offset.x), -int(camera_offset.y))

        return self._current_image, rect_camera

    def update(self, delta_time: float):
        super().update(delta_time)

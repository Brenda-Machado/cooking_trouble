"""
Cooking Trouble.

Classe que representa o inimigo humanóide.

enemy_person.py
"""

from src.models.entities.base.movable_entity import MovableEntity
from src.utils.coordinate import Coordinate
from src.utils.size import Size
from src.utils.constants import ENEMY_PERSON_SIZE, ENEMY_PERSON_SPEED, ENEMY_DETECTION_RADIUS, ENEMY_PATROL_RADIUS
from src.services.image_manager import ImageManager

class EnemyPerson(MovableEntity):
    def __init__(self, spawn_coord: Coordinate, detection_radius: float = ENEMY_DETECTION_RADIUS,
                 patrol_radius: float = ENEMY_PATROL_RADIUS):
        super().__init__(spawn_coord, Size(*ENEMY_PERSON_SIZE), ENEMY_PERSON_SPEED)
        self._spawn_coord = Coordinate(spawn_coord.x, spawn_coord.y)
        self._detection_radius = detection_radius
        self._patrol_radius = patrol_radius
        self._images = self.load_images([
            'idle_up', 'idle_down', 'walk_left_1', 'walk_left_2',
            'walk_right_1', 'walk_right_2', 'hurt_up', 'hurt_down'
        ])
        self._current_image = self._images

    @property
    def spawn_coord(self) -> Coordinate:
        return self._spawn_coord

    @property
    def detection_radius(self) -> float:
        return self._detection_radius

    def decide_direction(self, player_coord: Coordinate = None):
        if self.is_knockbacked:
            return  

        if player_coord and self._coord.distance_to(player_coord) <= self._detection_radius:
            self.direction = Coordinate.unit_vector(self._coord, player_coord)
            return

        distance_to_spawn = self._coord.distance_to(self._spawn_coord)

        if distance_to_spawn > self._patrol_radius:
            self.direction = Coordinate.unit_vector(self._coord, self._spawn_coord)
            return

        self.direction = Coordinate(0, 0)

    def on_collision(self, other_coord: Coordinate):
        self.apply_knockback(other_coord, 30)

    def load_images(self, sprite_names: list) -> list:
        image_manager = ImageManager()
        images = []

        for name in sprite_names:
            img = image_manager.get_sprite(
                'enemy_person', name,
                self._size.width,
                self._size.height
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
        rect_camera = self._rect.move(
            -int(camera_offset.x),
            -int(camera_offset.y)
        )
        
        return self._current_image, rect_camera

    def update(self, delta_time: float):
        super().update(delta_time)

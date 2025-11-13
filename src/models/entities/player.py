"""
Cooking Trouble.

Classe que representa o jogador.

player.py
"""

from src.models.entities.base.movable_entity import MovableEntity
from src.utils.coordinate import Coordinate
from src.utils.size import Size
from src.utils.constants import PLAYER_SIZE, PLAYER_SPEED
from src.services.image_manager import ImageManager

class Player(MovableEntity):
    def __init__(self, coord: Coordinate):
        super().__init__(coord, Size(*PLAYER_SIZE), PLAYER_SPEED)
        self._carrying_item = None
        self._images = self.load_images([
            'idle_up', 'idle_down', 'walk_left_1', 'walk_left_2',
            'walk_right_1', 'walk_right_2', 'hurt_up', 'hurt_down'
        ])
        self._current_image = self._images

    @property
    def carrying_item(self):
        return self._carrying_item

    @carrying_item.setter
    def carrying_item(self, item):
        self._carrying_item = item

    def pick_up_item(self, item) -> bool:
        if not item.is_active:
            return False

        if self._coord.distance_to(item.coord) > item.interaction_radius:
            return False

        self._carrying_item = item
        item.deactivate()

        return True

    def drop_item(self):
        if self._carrying_item:
            self._carrying_item.activate()
            self._carrying_item = None

    def deliver_item(self, delivery_point) -> bool:
        if not self._carrying_item:
            return False

        if self._coord.distance_to(delivery_point.coord) > delivery_point.interaction_radius:
            return False

        self._carrying_item = None

        return True

    def decide_direction(self, keys: dict):

        if self.is_knockbacked:
            return

        horizontal = 0
        vertical = 0

        if keys.get('w', False):
            vertical -= 1
        if keys.get('s', False):
            vertical += 1
        if keys.get('d', False):
            horizontal += 1
        if keys.get('a', False):
            horizontal -= 1

        self.direction = Coordinate.unit_vector(
            Coordinate(0, 0),
            Coordinate(horizontal, vertical)
        )

    def on_collision(self, other_coord: Coordinate):
        self.apply_knockback(other_coord, 30)

        if self._carrying_item:
            self.drop_item()

    def load_images(self, sprite_names: list) -> list:
        image_manager = ImageManager()
        images = []

        for name in sprite_names:
            img = image_manager.get_sprite(
                'player', name,
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

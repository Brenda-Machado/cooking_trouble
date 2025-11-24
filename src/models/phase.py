"""
Cooking Trouble.

Modelo de fase.

phase.py
"""

from typing import List, Dict, Optional
from math import floor, ceil
from src.models.entities.player import Player
from src.models.entities.enemy_person import EnemyPerson
from src.models.entities.enemy_obstacle import EnemyObstacle
from src.models.entities.item import Item
from src.models.entities.delivery_point import DeliveryPoint
from src.models.entities.map import GameMap
from src.utils.coordinate import Coordinate
from src.services.sound_manager import SoundManager
from src.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Phase:
    def __init__(self, player: Player, person_enemies: List[EnemyPerson],
                 obstacle_enemies: List[EnemyObstacle], game_map: GameMap,
                 delivery_points: List[DeliveryPoint], items: List[Item]):
        self._player = player
        self._person_enemies = person_enemies
        self._obstacle_enemies = obstacle_enemies
        self._map = game_map
        self._delivery_points = delivery_points
        self._items = items
        self._active_item: Optional[Item] = None
        self._active_delivery_point: Optional[DeliveryPoint] = None
        self._is_victory = False
        self._sound_manager = SoundManager()

        self._spawn_next_item()

    @property
    def player(self) -> Player:
        return self._player

    @property
    def person_enemies(self) -> List[EnemyPerson]:
        return self._person_enemies

    @property
    def obstacle_enemies(self) -> List[EnemyObstacle]:
        return self._obstacle_enemies

    @property
    def map(self) -> GameMap:
        return self._map

    @property
    def delivery_points(self) -> List[DeliveryPoint]:
        return self._delivery_points

    @property
    def active_item(self) -> Optional[Item]:
        return self._active_item

    @property
    def active_delivery_point(self) -> Optional[DeliveryPoint]:
        return self._active_delivery_point

    @property
    def is_victory(self) -> bool:
        return self._is_victory

    def update(self, movement_input: Dict[str, bool], interact: bool, delta_time: float):
        self._player.decide_direction(movement_input)

        for enemy in self._person_enemies:
            enemy.decide_direction(self._player.coord)

        for enemy in self._obstacle_enemies:
            enemy.decide_direction()

        all_entities = [
            self._player,
            *self._person_enemies,
            *self._obstacle_enemies
        ]

        for entity in all_entities:
            self._resolve_map_collision(entity)
            entity.update(delta_time)

        self._resolve_entity_collisions(all_entities)

        if interact:
            self._handle_item_interaction()

    def _spawn_next_item(self):
        if len(self._items) > 0:
            self._active_item = self._items.pop(0)
            self._active_item.coord = self._map.get_random_item_spawn()
            self._active_delivery_point = self._delivery_points[int(len(self._delivery_points) * 0.5)]
        else:
            self._active_item = None
            self._active_delivery_point = None
            self._is_victory = True

    def _handle_item_interaction(self):
        if self._active_item and not self._player.carrying_item:

            if self._player.pick_up_item(self._active_item):
                self._sound_manager.play_sound('pickup_item')

        elif self._player.carrying_item and self._active_delivery_point:

            if self._player.deliver_item(self._active_delivery_point):
                self._sound_manager.play_sound('item_delivered')
                self._spawn_next_item()

    def _resolve_map_collision(self, entity):
        dx = entity.direction.x * entity.get_effective_speed()
        dy = entity.direction.y * entity.get_effective_speed()
        dx = ceil(dx) if dx >= 0 else floor(dx)
        dy = ceil(dy) if dy >= 0 else floor(dy)

        if (entity.rect.left + dx <= 0 or entity.rect.right + dx >= self._map.width):
            entity.direction.x = 0

        if (entity.rect.top + dy <= 0 or entity.rect.bottom + dy >= self._map.height):
            entity.direction.y = 0

        obstacles = self._map.get_obstacle_rects()

        collide_xy = entity.rect.move(dx, dy).collidelist(obstacles) != -1
        collide_x = entity.rect.move(dx, 0).collidelist(obstacles) != -1
        collide_y = entity.rect.move(0, dy).collidelist(obstacles) != -1

        if collide_xy and not (collide_x or collide_y):
            entity.direction.x = 0
            entity.direction.y = 0
        elif collide_x:
            entity.direction.x = 0
        elif collide_y:
            entity.direction.y = 0

    def _resolve_entity_collisions(self, entities: List):
        for i, entity_i in enumerate(entities):

            for j in range(i + 1, len(entities)):
                entity_j = entities[j]

                if entity_i.collides_with(entity_j):
                    self._sound_manager.play_sound('collision')
                    entity_i.on_collision(entity_j.coord)
                    entity_j.on_collision(entity_i.coord)

    def get_camera_position(self) -> Coordinate:
        camera_x = self._player.coord.x - SCREEN_WIDTH / 2
        camera_y = self._player.coord.y - SCREEN_HEIGHT / 2
        camera_x = max(0, min(camera_x, self._map.width - SCREEN_WIDTH))
        camera_y = max(0, min(camera_y, self._map.height - SCREEN_HEIGHT))

        return Coordinate(camera_x, camera_y)

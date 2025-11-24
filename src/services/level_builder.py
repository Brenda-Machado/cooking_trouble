"""
Cooking Trouble.

Construtor de fases com padrão Builder.

level_builder.py
"""

from src.models.phase import Phase
from src.models.entities.player import Player
from src.models.entities.enemy_person import EnemyPerson
from src.models.entities.enemy_obstacle import EnemyObstacle
from src.models.entities.item import Item
from src.models.entities.delivery_point import DeliveryPoint
from src.models.entities.map import GameMap
from src.utils.coordinate import Coordinate
from src.utils.constants import DifficultyLevel
from random import randrange
from math import ceil
from copy import deepcopy

class LevelBuilder:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):
        self._map_library = {} 

    def build_phase(self, level_name: str, difficulty: int) -> Phase:
        map_data = self._load_map_data(level_name)
        game_map = self._create_map(map_data)

        player = Player(Coordinate(
            map_data['player_spawn']['x'],
            map_data['player_spawn']['y']
        ))

        enemies_person = self._create_person_enemies(
            map_data, difficulty
        )
        enemies_obstacle = self._create_obstacle_enemies(
            map_data, difficulty
        )

        delivery_points = self._create_delivery_points(map_data)
        items = self._create_items(map_data, difficulty)

        return Phase(
            player, enemies_person, enemies_obstacle,
            game_map, delivery_points, items
        )

    def _load_map_data(self, level_name: str) -> dict:
        return {
            'player_spawn': {'x': 640, 'y': 360},
            'enemy_spawns': [
                {'x': 200, 'y': 200},
                {'x': 1000, 'y': 500}
            ],
            'delivery_points': [
                {'x': 100, 'y': 100},
                {'x': 1100, 'y': 600}
            ],
            'item_spawns': [
                {'x': 300, 'y': 300},
                {'x': 800, 'y': 400}
            ]
        }

    def _create_map(self, map_data: dict) -> GameMap:
        return GameMap(
            map_name=map_data.get('name', 'default'),
            width=1280,
            height=720
        )

    def _create_person_enemies(self, map_data: dict, difficulty: int) -> list:
        num_enemies = self._calculate_enemy_count(
            len(map_data.get('enemy_spawns', [])), difficulty
        )

        enemies = []
        spawns = map_data.get('enemy_spawns', [])

        for i in range(min(num_enemies, len(spawns))):
            spawn = spawns[i]
            enemy = EnemyPerson(
                Coordinate(spawn['x'], spawn['y']),
                detection_radius=300 + difficulty * 50,
                patrol_radius=50 + difficulty * 20
            )
            enemies.append(enemy)

        return enemies

    def _create_obstacle_enemies(self, map_data: dict, difficulty: int) -> list:
        return []

    def _create_delivery_points(self, map_data: dict) -> list:
        points = []

        for point_data in map_data.get('delivery_points', []):
            point = DeliveryPoint(
                Coordinate(point_data['x'], point_data['y'])
            )
            points.append(point)

        return points

    def _create_items(self, map_data: dict, difficulty: int) -> list:
        items = []
        num_items = 1 + difficulty * 2
        spawns = map_data.get('item_spawns', [])

        for i in range(num_items):
            spawn = spawns[i % len(spawns)]
            item = Item(
                Coordinate(spawn['x'], spawn['y']),
                item_type='default'
            )
            items.append(item)

        return items

    @staticmethod
    def _calculate_enemy_count(base_count: int, difficulty: int) -> int:
        return ceil((difficulty + 1) / 3 * base_count)

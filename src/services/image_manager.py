"""
Cooking Trouble.

Gerenciador Singleton centralizado de imagens com cache.

image_manager.py
"""

import pygame
import os
from typing import Dict

class ImageManager:
    _instance = None
    _cache: Dict[str, pygame.Surface] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._asset_path = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'images')

    def get_sprite(self, category: str, name: str, width: int, height: int) -> pygame.Surface:
        cache_key = f"{category}_{name}_{width}_{height}"

        if cache_key in self._cache:
            return self._cache[cache_key]

        file_path = os.path.join(self._asset_path, category, f"{name}.png")

        try:
            image = pygame.image.load(file_path).convert_alpha()
            image = pygame.transform.scale(image, (width, height))
            self._cache[cache_key] = image

            return image
        
        except pygame.error as e:
            print(f"Erro ao carregar sprite {file_path}: {e}")

            return pygame.Surface((width, height))

    def get_background(self, name: str, width: int, height: int) -> pygame.Surface:
        return self.get_sprite('maps', name, width, height)

    def clear_cache(self):
        self._cache.clear()

    def get_cache_info(self) -> Dict:
        return {
            'cached_images': len(self._cache),
            'total_memory': sum(
                img.get_size() * img.get_size() * 4
                for img in self._cache.values()
            )
        }

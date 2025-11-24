"""
Cooking Trouble.

Renderizador principal.

renderer.py
"""

import pygame
from typing import Tuple
from src.utils.coordinate import Coordinate
from src.utils.constants import COLOR_WHITE, COLOR_BLACK
from src.models.phase import Phase

class GameRenderer:
    def __init__(self, screen_size: Tuple[int, int]):
        self._screen_width, self._screen_height = screen_size
        self._font_name = 'PressStart2P-vaV7.ttf'

    def render_phase(self, display: pygame.Surface, phase: Phase,
                     camera_offset: Coordinate, timer_seconds: int):
        display.fill(COLOR_BLACK)

        self._render_map(display, phase.map, camera_offset)
        self._render_delivery_points(display, phase.delivery_points, camera_offset)
        self._render_moving_entities(display, phase, camera_offset)

        if phase.active_item:
            self._render_item(display, phase.active_item, camera_offset)

        self._render_ui(display, timer_seconds)
        self._render_compass(
            display, phase.player, phase.active_item,
            phase.active_delivery_point, camera_offset
        )

    def _render_map(self, display: pygame.Surface, game_map, camera_offset: Coordinate):
        map_data = game_map.get_render_data(camera_offset)

        for image, rect in map_data:
            if image and rect:
                display.blit(image, rect)

    def _render_delivery_points(self, display: pygame.Surface, points: list,
                                camera_offset: Coordinate):
        for point in points:
            image, rect = point.draw(camera_offset)

            if image and rect:
                display.blit(image, rect)

    def _render_moving_entities(self, display: pygame.Surface, phase: Phase,
                                camera_offset: Coordinate):
        all_entities = (
            [phase.player] +
            phase.person_enemies +
            phase.obstacle_enemies
        )

        for entity in all_entities:
            image, rect = entity.draw(camera_offset)

            if image and rect:
                display.blit(image, rect)

    def _render_item(self, display: pygame.Surface, item,
                     camera_offset: Coordinate):
        image, rect = item.draw(camera_offset)

        if image and rect:
            display.blit(image, rect)

    def _render_ui(self, display: pygame.Surface, timer_seconds: int):
        timer_text = self._format_timer(timer_seconds)

        self._draw_bordered_text(
            display, timer_text, 38,
            self._screen_width / 2, 40,
            COLOR_WHITE, COLOR_BLACK
        )

        self._draw_bordered_text(
            display, 'Pausar: ESC', 25,
            150, 30, COLOR_WHITE, COLOR_BLACK
        )

    def _render_compass(self, display: pygame.Surface, player,
                        item, delivery_point, camera_offset: Coordinate):
        if not delivery_point and not item:
            return

        if item and item.is_active:
            target = item.coord
            color = (128, 0, 0) 
        else:
            target = delivery_point.coord
            color = (255, 140, 0)

        self._draw_compass_triangle(
            display, player.coord, target, camera_offset, color
        )

    def _draw_compass_triangle(self, display: pygame.Surface,
                               from_coord: Coordinate, to_coord: Coordinate,
                               camera_offset: Coordinate, color: Tuple):
        vector = Coordinate.unit_vector(from_coord, to_coord)

        tip = (
            from_coord.x + vector.x * 80 - camera_offset.x,
            from_coord.y + vector.y * 80 - camera_offset.y
        )
        base_left = (
            from_coord.x + vector.x * 55 - camera_offset.x + 5,
            from_coord.y + vector.y * 55 - camera_offset.y + 5
        )
        base_right = (
            from_coord.x + vector.x * 55 - camera_offset.x - 5,
            from_coord.y + vector.y * 55 - camera_offset.y - 5
        )

        pygame.draw.polygon(display, color, [tip, base_left, base_right])

    def _draw_bordered_text(self, display: pygame.Surface, text: str,
                            size: int, x: float, y: float,
                            text_color: Tuple, border_color: Tuple):
        font = pygame.font.Font(self._font_name, size)
        text_surface = font.render(text, True, text_color)
        border_surface = font.render(text, True, border_color)
        text_rect = text_surface.get_rect(center=(x, y))

        for offset in [(-2, -2), (-2, 2), (2, -2), (2, 2)]:
            display.blit(border_surface, text_rect.move(*offset))

        display.blit(text_surface, text_rect)

    @staticmethod
    def _format_timer(seconds: int) -> str:
        minutes = seconds // 60
        secs = seconds % 60

        return f"{minutes:02d}:{secs:02d}"

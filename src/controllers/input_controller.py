"""
Cooking Trouble.

Controlador de inputs do teclado.

input_controller.py
"""

import pygame
from pygame.locals import *

class InputController:
    def __init__(self):
        self._pressed_keys = {
            'w': False, 'a': False, 's': False, 'd': False,
            'space': False, 'esc': False, 'enter': False,
            'backspace': False
        }
        self._events = []

    def update(self):
        self._pressed_keys = {
            'w': False, 'a': False, 's': False, 'd': False,
            'space': False, 'esc': False, 'enter': False,
            'backspace': False
        }
        self._events = []

        for event in pygame.event.get():
            self._events.append(event)

            if event.type == QUIT:
                return False

            if event.type == KEYDOWN:
                if event.key == K_w:
                    self._pressed_keys['w'] = True
                elif event.key == K_a:
                    self._pressed_keys['a'] = True
                elif event.key == K_s:
                    self._pressed_keys['s'] = True
                elif event.key == K_d:
                    self._pressed_keys['d'] = True
                elif event.key == K_SPACE:
                    self._pressed_keys['space'] = True
                elif event.key == K_ESCAPE:
                    self._pressed_keys['esc'] = True
                elif event.key == K_RETURN:
                    self._pressed_keys['enter'] = True
                elif event.key == K_BACKSPACE:
                    self._pressed_keys['backspace'] = True

        return True

    def get_movement_input(self) -> dict:
        return {
            'w': self._pressed_keys['w'],
            'a': self._pressed_keys['a'],
            's': self._pressed_keys['s'],
            'd': self._pressed_keys['d']
        }

    def get_action_input(self) -> dict:
        return {
            'interact': self._pressed_keys['space'],
            'pause': self._pressed_keys['esc'],
            'confirm': self._pressed_keys['enter'],
            'back': self._pressed_keys['backspace']
        }

    def get_keys_pressed(self) -> dict:
        return self._pressed_keys.copy()

    def get_events(self) -> list:
        return self._events

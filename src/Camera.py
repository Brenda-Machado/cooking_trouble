from sys import implementation
import pygame
from Coordenada import Coordenada
from Tamanho import Tamanho


class Camera:
    def __init__(self, jogador_rect: pygame.Rect, tamanho_display):
        self.__jogador_rect = jogador_rect
        self.__posicao_int = Coordenada(0, 0)
        self.__posicao_float = Coordenada(0, 0)
        self.__largura_display = tamanho_display[0]
        self.__altura_display = tamanho_display[1]

    def moverCamera(self):
        self.__posicao_float.x += (self.__jogador_rect.x -
                                   self.__posicao_float.x)
        self.__posicao_float.y += (self.__jogador_rect.y -
                                   self.__posicao_float.y)
        self.__posicao_int.x, self.__posicao_int.y = int(
            self.__posicao_float.x), int(self.__posicao_float.y)
        self.__posicao_int.x = max(
            self.__jogador_rect.left, self.__posicao_int.x)
        self.__posicao_int.x = min(
            self.__posicao_int.x, self.__jogador_rect.right - self.__largura_display/2)
        self.__posicao_int.y = max(
            self.__jogador_rect.top, self.__posicao_int.y)
        self.__posicao_int.y = min(
            self.__posicao_int.y, self.__jogador_rect.top - self.__altura_display/2)

    @property
    def posicao_int(self):
        return self.__posicao_int

from cmath import rect
from Coordenada import Coordenada
from abc import ABC, abstractmethod
import pygame


class Interativos(ABC):
    def __init__(self, raio_interacao: float = None, coordenada: Coordenada = None):
        self.__raio_interacao = raio_interacao
        self.__coord = coordenada
        self.__ativo = False
        self.__rect = None

    @ property
    def raio_interacao(self) -> float:
        return self.__raio_interacao

    @ property
    def coord(self) -> Coordenada:
        return self.__coord

    @ property
    def ativo(self) -> bool:
        return self.__ativo

    @ property
    def rect(self) -> pygame.Rect:
        return self.__rect

    @ coord.setter
    def coord(self, coord: Coordenada):
        self.__coord = coord

    @ ativo.setter
    def ativo(self, ativo: bool):
        self.__ativo = ativo

    @ rect.setter
    def rect(self, rect: pygame.Rect):
        self.__rect = rect

    @abstractmethod
    def desenhar(self, posicao_camera):
        pass

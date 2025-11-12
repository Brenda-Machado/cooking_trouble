from src.utils.Coordenada import Coordenada
from Interativos import Interativos
import pygame
from GerenciadorImagens import GerenciadorImagens


class Item(Interativos):
    def __init__(self, nome: str):
        self.__nome = nome
        self.__tamanho_lado = 35
        super().__init__(80)
        self.__imagem = GerenciadorImagens().getSprite(
            'item', self.__nome, self.__tamanho_lado, self.__tamanho_lado)

    def criar(self, coordenada: Coordenada):
        self.coord = coordenada
        self.ativo = True
        self.rect = pygame.Rect(
            self.coord.x, self.coord.y, self.__tamanho_lado, self.__tamanho_lado)
        return self

    def desenhar(self, posicao_camera):
        self.rect.center = (self.coord.x, self.coord.y)
        rect_camera = self.rect.move(-posicao_camera.x, -posicao_camera.y)
        return self.__imagem, rect_camera

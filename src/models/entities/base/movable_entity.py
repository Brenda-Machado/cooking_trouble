import pygame
from src.utils.Coordenada import Coordenada
from src.utils.Tamanho import Tamanho
from abc import ABC, abstractmethod
from GerenciadorImagens import GerenciadorImagens


class Movel(ABC):
    def __init__(self, coord: Coordenada, tamanho: Tamanho, velocidade: float, sprites: list = []):
        self.__coord = coord
        self.__tamanho = tamanho
        self.__velocidade = velocidade
        self.__direcao_deslocamento = Coordenada(0, 0)
        self.__rect = pygame.Rect((self.coord.x, self.coord.y, int(
            self.tamanho.largura), int(self.tamanho.altura)))
        self.__atingido = False
        self.__coord_atingido = None
        self.__angulo = 0
        self.__imagens = self.salvar_imagens(sprites)

    @abstractmethod
    # define self.__direcao_deslocamento com base no estado (comando do jogador ou decisao de IA)
    def decideDirecao(self):
        pass

    # define o que acontece quando o objeto colide com outro objeto (na coordenada coord)
    def colidiu(self, coord: Coordenada):
        pass

    @abstractmethod
    def salvar_imagens(self, sprites: list):
        pass

    @property
    def coord(self) -> Coordenada:
        return self.__coord

    @property
    def tamanho(self) -> Tamanho:
        return self.__tamanho

    @property
    def velocidade(self) -> float:
        return self.__velocidade

    @property
    def direcao_deslocamento(self) -> Coordenada:
        return self.__direcao_deslocamento

    @property
    def rect(self):
        return self.__rect

    @property
    def atingido(self) -> int:
        return self.__atingido

    @property
    def coord_atingido(self) -> Coordenada:
        return self.__coord_atingido

    @property
    def angulo(self) -> int:
        return self.__angulo

    @property
    def imagens(self):
        return self.__imagens

    @coord.setter
    def coord(self, coord: Coordenada):
        self.__coord = coord

    @imagens.setter
    def imagens(self, imagens: list):
        self.__imagens = imagens

    @tamanho.setter
    def tamanho(self, tamanho: Tamanho):
        self.__tamanho.largura = tamanho.largura
        self.__tamanho.altura = tamanho.altura

    @velocidade.setter
    def velocidade(self, velocidade: float):
        self.__velocidade = velocidade

    @direcao_deslocamento.setter
    def direcao_deslocamento(self, dir: Coordenada):
        self.__direcao_deslocamento.x = dir.x
        self.__direcao_deslocamento.y = dir.y

        if self.direcao_deslocamento.x != 0 and self.direcao_deslocamento.y != 0:
            if abs(self.direcao_deslocamento.x) >= 0.924:
                if self.direcao_deslocamento.x > 0:
                    self.__angulo = 270
                else:
                    self.__angulo = 90
            elif abs(self.direcao_deslocamento.y) >= 0.924:
                if self.direcao_deslocamento.y > 0:
                    self.__angulo = 180
                else:
                    self.__angulo = 0
            else:
                if self.direcao_deslocamento.x > 0:
                    if self.direcao_deslocamento.y > 0:
                        self.__angulo = 225
                    else:
                        self.__angulo = 315
                else:
                    if self.direcao_deslocamento.y > 0:
                        self.__angulo = 135
                    else:
                        self.__angulo = 45

    @atingido.setter
    def atingido(self, atingido: int):
        self.__atingido = atingido

    @coord_atingido.setter
    def coord_atingido(self, coord: Coordenada):
        self.__coord_atingido = Coordenada(coord.x, coord.y)

    def desenhar(self, posicao_camera):
        rect_camera = self.__rect.move(-posicao_camera.x, -posicao_camera.y)
        return rect_camera

    def velocidade_real(self) -> float:
        return self.velocidade * 2 if self.atingido > 0 else self.velocidade

    def mover(self):
        if self.atingido > 0:
            self.atingido -= 1
        direcao = self.__direcao_deslocamento
        velocidade = self.velocidade_real()
        self.__coord.mover(direcao.x*velocidade,
                           direcao.y*velocidade)
        if self.angulo >= 315 or self.angulo <= 45 or (self.angulo >= 135 and self.angulo <= 225):
            self.__rect.update(0, 0, self.tamanho.largura, self.tamanho.altura)
        else:
            self.__rect.update(0, 0, self.tamanho.altura, self.tamanho.largura)
        self.__rect.center = self.coord.x, self.coord.y

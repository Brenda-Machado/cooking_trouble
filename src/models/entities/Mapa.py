from src.utils.Coordenada import Coordenada
from src.utils.Tamanho import Tamanho
from random import randrange
from ObstaculoMapa import ObstaculoMapa
from src.models.entities.PontoEntrega import PontoEntrega
import pygame
from GerenciadorImagens import GerenciadorImagens


class Mapa:
    def __init__(self, tamanho: Tamanho, spawn_jogador: Coordenada, spawn_inimigos_p: list,
                 caminhos_inimigos_o: list, spawn_itens: list,
                 pontos_entrega: list, obstaculos: list, local: str):
        self.__tamanho = tamanho
        self.__spawn_jogador = spawn_jogador
        self.__spawn_inimigos_p = spawn_inimigos_p
        self.__caminho_inimigos_o = caminhos_inimigos_o
        self.__spawn_itens = spawn_itens
        self.__pontos_entrega = pontos_entrega
        self.__obstaculos = obstaculos
        self.__imagem = GerenciadorImagens().getSprite(
            'mapa', local, tamanho.largura, tamanho.altura)
        self.__rect = self.__imagem.get_rect()
        self.__rect.topleft = (0, 0)

    # getters

    @ property
    def tamanho(self):
        return self.__tamanho

    @ property
    def spawn_jogador(self):
        return self.__spawn_jogador

    @ property
    def spawn_inimigos_p(self):
        return [*self.__spawn_inimigos_p]

    @ property
    def caminho_inimigos_o(self):
        return [*self.__caminho_inimigos_o]

    @ property
    def obstaculos(self):
        return [*self.__obstaculos]

    @ property
    def pontos_entrega(self) -> PontoEntrega:
        return [*self.__pontos_entrega]

    # métodos

    def coordItemAleatoria(self):
        n = randrange(len(self.__spawn_itens))
        return self.__spawn_itens[n]

    def coordEntregaAleatoria(self):
        n = randrange(len(self.__pontos_entrega))
        return self.__pontos_entrega[n]

    def desenhar(self, posicao_camera):
        rect_camera = self.__rect.move(-posicao_camera.x, -posicao_camera.y)
        dados = []
        dados.append((self.__imagem, rect_camera))
        for obstaculo in self.__obstaculos:
            dados.append(obstaculo.desenhar(posicao_camera))
        return dados

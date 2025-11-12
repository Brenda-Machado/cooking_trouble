import imp
import pygame
from Jogador import Jogador
from Item import Item
from InimigoObstaculo import InimigoObstaculo
from InimigoPessoa import InimigoPessoa
from PontoEntrega import PontoEntrega
from Movel import Movel
from ObstaculoMapa import ObstaculoMapa
from Mapa import Mapa
from random import randrange
from math import floor, ceil
from src.utils.Coordenada import Coordenada
from GerenciadorSons import GerenciadorSons


class Fase:

    def __init__(self, jogador: Jogador, inimigos_pessoa: list, inimigos_obstaculo: list, mapa: Mapa,
                 pontos_entrega: list, lista_itens: list):
        self.__jogador = jogador
        self.__inimigos_pessoa = inimigos_pessoa
        self.__inimigos_obstaculo = inimigos_obstaculo

        self.__mapa = mapa
        self.__lista_itens = [*lista_itens]
        self.__pontos_entrega = pontos_entrega

        self.__ponto_entrega_ativo = None
        self.__item_ativo = None
        self.proximoItem()
        self.__vitoria = False
        self.__som_colisao = GerenciadorSons().getSound('sons', 'colisao')
        self.__som_item = GerenciadorSons().getSound('sons', 'item')

    # GETTERS
    @property
    def jogador(self):
        return self.__jogador

    @property
    def ponto_entrega_ativo(self) -> PontoEntrega:
        return self.__ponto_entrega_ativo

    @property
    def inimigos_obstaculo(self):
        return self.__inimigos_obstaculo

    @property
    def item_ativo(self):
        return self.__item_ativo

    @item_ativo.setter
    def item_ativo(self, item):
        self.__item_ativo = item

    @property
    def inimigos_pessoa(self):
        return self.__inimigos_pessoa

    @property
    def mapa(self):
        return self.__mapa

    @property
    def lista_itens(self):
        return self.__lista_itens

    @property
    def pontos_entrega(self):
        return self.__pontos_entrega

    @property
    def vitoria(self):
        return self.__vitoria

    # METODOS

    def movimento(self, teclas: dict):
        self.jogador.decideDirecao(
            teclas['w'], teclas['s'], teclas['d'], teclas['a'])

        for inim in self.__inimigos_pessoa:
            inim.decideDirecao(self.__jogador.coord)

        for inim in self.__inimigos_obstaculo:
            inim.decideDirecao()

        for mov in (*self.__inimigos_pessoa, *self.__inimigos_obstaculo, self.__jogador):
            self.colisao_mapa(mov)
            mov.mover()

    def proximoItem(self):
        if len(self.lista_itens) > 0:
            self.__item_ativo = self.__lista_itens.pop(
                0).criar(self.mapa.coordItemAleatoria())
            self.__ponto_entrega_ativo = self.pontos_entrega[randrange(
                len(self.pontos_entrega))]
            return None
        self.__item_ativo = None
        self.__ponto_entrega_ativo = None
        self.__vitoria = True

    def gerenciamentoItem(self, comando_interagir_item: bool):
        if self.__item_ativo == None and self.__jogador.item_carregado == None:
            self.proximoItem()
        elif comando_interagir_item and self.__item_ativo != None:
            if self.__jogador.pegarItem(self.__item_ativo):
                self.__som_item.play()
                # acao se pegou

            if self.__jogador.entregarItem(self.ponto_entrega_ativo):
                self.item_ativo = None  # acao se entregou
                self.__som_item.play()
        return False

    def colisao_mapa(self, movel):
        deslocamento_x = movel.direcao_deslocamento.x*movel.velocidade_real()
        deslocamento_x = ceil(
            deslocamento_x) if deslocamento_x >= 0 else floor(deslocamento_x)

        deslocamento_y = movel.direcao_deslocamento.y*movel.velocidade_real()
        deslocamento_y = ceil(
            deslocamento_y) if deslocamento_y >= 0 else floor(deslocamento_y)

        lista_obstaculos = [obst.rect for obst in self.mapa.obstaculos]

        if (movel.rect.left+(deslocamento_x) <= 0 or
                movel.rect.right + (deslocamento_x) >= self.mapa.tamanho.largura):
            movel.direcao_deslocamento.x = 0
        if(movel.rect.top+(deslocamento_y) <= 0 or
           movel.rect.bottom + (deslocamento_y) >= self.mapa.tamanho.altura):
            movel.direcao_deslocamento.y = 0

        colide_xy = (movel.rect.move(deslocamento_x,
                     deslocamento_y).collidelist(lista_obstaculos) != -1)
        colide_x = movel.rect.move(
            deslocamento_x, 0).collidelist(lista_obstaculos) != -1
        colide_y = movel.rect.move(
            0, deslocamento_y).collidelist(lista_obstaculos) != -1
        if (colide_xy and not(colide_x or colide_y)):
            movel.direcao_deslocamento.x = 0
            movel.direcao_deslocamento.y = 0
        if (colide_x):
            movel.direcao_deslocamento.x = 0
        if (colide_y):
            movel.direcao_deslocamento.y = 0

    def colisao_moveis(self):
        num_moveis = len(
            (self.__jogador, *self.__inimigos_pessoa, *self.__inimigos_obstaculo))
        lista_moveis = [self.__jogador, *
                        self.__inimigos_pessoa, *self.__inimigos_obstaculo]
        for i in range(num_moveis):
            movel_i = lista_moveis[i]
            if i+1 < num_moveis:
                for j in range(i+1, num_moveis):
                    movel_j = lista_moveis[j]
                    if movel_i.rect.colliderect(movel_j.rect):
                        self.__som_colisao.set_volume(0.3)
                        self.__som_colisao.play()
                        movel_i.colidiu(movel_j.coord)
                        movel_j.colidiu(movel_i.coord)

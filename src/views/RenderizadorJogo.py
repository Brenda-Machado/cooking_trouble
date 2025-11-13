from typing import Tuple
import pygame
import sys
from pygame.locals import *
from GerenciadorImagens import GerenciadorImagens
from src.models.entities.Mapa import Mapa
from src.models.entities.PontoEntrega import PontoEntrega
from src.models.entities.Item import Item
from InimigoObstaculo import InimigoObstaculo
from InimigoPessoa import InimigoPessoa
from src.models.entities.player import Jogador
from src.utils.Coordenada import Coordenada
from src.utils.Tamanho import Tamanho
import time


class RenderizadorJogo():
    def __init__(self, tamanho: Tuple):
        self.__tamanho_display = self.__largura, self.__altura = tamanho[0], tamanho[1]
        self.__fonte = 'PressStart2P-vaV7.ttf'

    def renderizar(self, display: pygame.display, posicao_camera: int, mapa: Mapa,
                   ponto_entrega: PontoEntrega, inimigos_p, inimigos_o, jogador: Jogador, item: Item, timer_sec):
        display.fill((0, 0, 0))
        for x in mapa.desenhar(posicao_camera):
            display.blit(x[0], x[1])
        if isinstance(ponto_entrega, PontoEntrega):
            dados_pe = ponto_entrega.desenhar(posicao_camera)
            display.blit(dados_pe[0], dados_pe[1])
        for movel in (*inimigos_p, *inimigos_o, jogador):
            dado_mov = movel.desenhar(posicao_camera)
            display.blit(dado_mov[0], dado_mov[1])
        if isinstance(item, Item) and item.ativo:
            dados_item = item.desenhar(posicao_camera)
            display.blit(dados_item[0], dados_item[1])

        preto = (0, 0, 0)
        branco = (255, 255, 255)

        texto_timer = (time.strftime('%M:%S', time.gmtime(timer_sec)))
        self.escreve_com_borda(display, texto_timer, 38, self.__largura/2, 40, branco, preto)

        self.escreve_com_borda(display, 'Pausar: esc', 25, 150, 30, branco, preto)

        self.desenhar_bussola_interativos(
            display, posicao_camera, ponto_entrega, item, jogador)

    def desenhar_bussola_interativos(self, display, posicao_camera, ponto_entrega, item, jogador):
        if ponto_entrega != None or item != None:
            if (item != None and item.ativo == True):
                destino = item.coord
                cor = (128, 0, 0)
            elif ponto_entrega != None:
                destino = ponto_entrega.coord
                cor = (255, 140, 0)
            vetor = Coordenada.versorEntreCoordenadas(jogador.coord, destino)

            ponta_triangulo = ((jogador.coord.x+vetor.x*jogador.tamanho.largura*1.5 - posicao_camera.x),
                               (jogador.coord.y+vetor.y*jogador.tamanho.altura*1.5 - posicao_camera.y))
            base_esquerda = ((jogador.coord.x+vetor.x*jogador.tamanho.largura - posicao_camera.x + 5),
                             (jogador.coord.y+vetor.y*jogador.tamanho.altura - posicao_camera.y + 5))
            base_direita = ((jogador.coord.x+vetor.x*jogador.tamanho.largura - posicao_camera.x - 5),
                            (jogador.coord.y+vetor.y*jogador.tamanho.altura - posicao_camera.y - 5))
            pygame.draw.polygon(display, cor, points=[
                                ponta_triangulo, base_direita, base_esquerda])

    def escreve_com_borda(self, display, texto, tamanho, x, y, cor_dentro, cor_fora):
        font = pygame.font.Font(self.__fonte, tamanho)
        text_surface = font.render(texto, True, cor_dentro)
        text_borda = font.render(texto, True, cor_fora)

        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)

        display.blit(text_borda, text_rect.move(-2, -2))
        display.blit(text_borda, text_rect.move(-2, +2))
        display.blit(text_borda, text_rect.move(+2, -2))
        display.blit(text_borda, text_rect.move(+2, +2))

        display.blit(text_surface, text_rect)

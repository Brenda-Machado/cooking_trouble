import pygame
from pygame.locals import *
from src.base_menu import Menu
from GerenciadorImagens import GerenciadorImagens


class MenuPausa(Menu):
    def __init__(self, tamanho):
        super().__init__(tamanho)
        self.__fundo_pausa = GerenciadorImagens().getSprite('fundo_menu', 'fundo_menu', 
        3*self.largura/4, 3*self.altura/4)
        self.__rect = self.__fundo_pausa.get_rect()

    def display_menu(self):
        self.__rect.center = (self.largura/2, self.altura/2)
        
        surface = pygame.Surface((self.largura, self.altura))
        surface.set_alpha(150)
        surface.fill((0, 0, 0))
        self.display.blit(surface, (0, 0))

        self.display.blit(self.__fundo_pausa, self.__rect)
        self.desenha_texto('Jogo pausado', 60, self.largura / 2,
                           self.altura / 6, self.branco, self.fonte)
        self.desenha_texto("Andar para Direita:  D", 20, self.largura/2,
                           self.altura/2 - 190, self.branco, self.fonte)
        self.desenha_texto("Andar para Esquerda: A", 20, self.largura/2,
                           self.altura/2 - 140, self.branco, self.fonte)
        self.desenha_texto("Andar para Cima: W", 20, self.largura/2,
                           self.altura/2 - 90, self.branco, self.fonte)
        self.desenha_texto("Andar para Baixo: S", 20, self.largura/2,
                           self.altura/2 - 40, self.branco, self.fonte)
        self.desenha_texto("Pegar Item: Espaço", 20, self.largura/2,
                           self.altura/2 + 10, self.branco, self.fonte)
        self.desenha_texto("Entregar Item: Espaço", 20, self.largura/2,
                           self.altura/2 + 60, self.branco, self.fonte)
        self.desenha_texto("Menu Principal: Backspace", 24, self.largura/2,
                           self.altura/2 + 200, self.branco, self.fonte)
        self.desenha_texto("Continuar: Esc/Enter", 24, self.largura/2,
                           self.altura/2 + 250, self.branco, self.fonte)

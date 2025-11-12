import pygame
from pygame.locals import *
from Menu import Menu
from GerenciadorImagens import GerenciadorImagens

class MenuDerrota(Menu):
    def __init__(self, tamanho):
        super().__init__(tamanho)
        self.__altura_derrota = self.altura/2 - 120

    def display_menu(self):
        self.display.fill((0, 0, 0))
        self.display.blit(self.fundo, (0,0))

        self.desenha_texto('Derrota', 60, self.largura/2,
        self.__altura_derrota, self.branco, self.fonte)

        self.desenha_texto("Tentar Novamente: Enter", 20, self.largura/2,
        self.altura/2, self.branco, self.fonte)
        self.desenha_texto("Voltar: Backspace", 20, self.largura/2,
        self.altura/2 + 60, self.branco, self.fonte)
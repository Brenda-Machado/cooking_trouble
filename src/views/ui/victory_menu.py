import pygame
from pygame.locals import *
from src.base_menu import Menu
from GerenciadorImagens import GerenciadorImagens

class MenuVitoria(Menu):
    def __init__(self, tamanho):
        super().__init__(tamanho)
        self.__altura_vitoria = self.altura/2 - 120

    def display_menu(self):
        self.display.fill((0, 0, 0))
        self.display.blit(self.fundo, (0, 0))
        
        self.desenha_texto("Vitória", 60, self.largura/2,
                        self.__altura_vitoria, self.branco, self.fonte)

        self.desenha_texto("Voltar: Backspace", 20, self.largura/2,
                           self.altura/2, self.branco, self.fonte)
        self.desenha_texto("Continuar: Enter", 20, self.largura/2,
                           self.altura/2 + 60, self.branco, self.fonte)
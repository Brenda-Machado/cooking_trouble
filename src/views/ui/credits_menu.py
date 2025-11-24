import pygame
from pygame.locals import *
from src.base_menu import Menu
from GerenciadorImagens import GerenciadorImagens


class MenuCreditos(Menu):
    def __init__(self, tamanho):
        super().__init__(tamanho)

    def display_menu(self):
        self.display.fill((0, 0, 0))
        self.display.blit(self.fundo, (0, 0))
        self.desenha_texto('Créditos', 60, self.largura / 2,
                           self.altura / 8, self.branco, self.fonte)
        self.desenha_texto('Arthur Torres de Lino', 25, self.largura / 2,
                           self.altura / 2 - 30, self.branco, self.fonte)
        self.desenha_texto('Brenda Silva Machado', 25, self.largura / 2,
                           self.altura / 2 - 90, self.branco, self.fonte)
        self.desenha_texto('Gabriela Furtado da Silveira', 25, self.largura /
                           2, self.altura / 2 - 150, self.branco, self.fonte)
        self.desenha_texto("Voltar: Backspace", 20, self.largura/2 - 200,
                           self.altura/2 + 190, self.branco, self.fonte)

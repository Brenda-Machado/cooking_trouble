import pygame
from pygame.locals import *
from Menu import Menu
from GerenciadorImagens import GerenciadorImagens

class MenuTutorial(Menu):
    def __init__(self, tamanho):
        super().__init__(tamanho)
           
    def display_menu(self):
        self.display.fill((0, 0, 0))
        self.display.blit(self.fundo, (0,0))
        self.desenha_texto('Tutorial', 60, self.largura / 2,
                           self.altura / 8, self.branco, self.fonte)
        self.desenha_texto("Andar para Direita:  D", 25, self.largura/2,
                           self.altura/2 - 190, self.branco, self.fonte)
        self.desenha_texto("Andar para Esquerda: A", 25, self.largura/2,
                           self.altura/2 - 140, self.branco, self.fonte)
        self.desenha_texto("Andar para Cima: W", 25, self.largura/2,
                           self.altura/2 - 90, self.branco, self.fonte)
        self.desenha_texto("Andar para Baixo: S", 25, self.largura/2,
                           self.altura/2 - 40, self.branco, self.fonte)
        self.desenha_texto("Pegar Item: Espaço", 25, self.largura/2,
                           self.altura/2 + 10, self.branco, self.fonte)
        self.desenha_texto("Entregar Item: Espaço", 25, self.largura/2,
                           self.altura/2 + 60, self.branco, self.fonte)
        self.desenha_texto("Pausa: Esc", 25, self.largura/2,
                           self.altura/2 + 110, self.branco, self.fonte)                   
        self.desenha_texto("Voltar: Backspace", 20, self.largura/2 - 200,
                           self.altura/2 + 190, self.branco, self.fonte)
                           
import pygame
from pygame.locals import *
from src.base_menu import Menu
from GerenciadorImagens import GerenciadorImagens

class MenuDificuldade(Menu):
    def __init__(self, tamanho):
        super().__init__(tamanho)        
        self.__opcao = 0
        self.__opcoes = [['Fácil', self.altura/2 - 60], ['Médio', self.altura/2], ['Difícil', self.altura/2 + 60]]

        self.__distancia_cursor = self.largura/2 - 150
        self.__cursor_rect = pygame.Rect(
            self.__distancia_cursor, self.__opcoes[0][1], 130, 130)

    @property
    def opcao(self):
        return self.__opcao
           
    def display_menu(self):
        self.display.fill((0, 0, 0))
        self.display.blit(self.fundo, (0,0))
        self.desenha_texto('Selecionar dificuldade', 60, self.largura / 2,
                           self.altura / 8, self.branco, self.fonte)
        for op in self.__opcoes:
            self.desenha_texto(op[0], 30, self.largura/2, op[1], self.branco, self.fonte)
        self.desenha_texto("Avançar: Enter", 20, self.largura/2 + 200,
                           self.altura/2 + 190, self.branco, self.fonte)       
        self.desenha_texto("Voltar: Backspace", 20, self.largura/2 - 200,
                           self.altura/2 + 190, self.branco, self.fonte)
        self.desenha_texto('▶', 20, self.__cursor_rect.x,
                           self.__cursor_rect.y, self.branco, self.fonte)
        
    def move_cursor(self, teclas_clicadas):
        if teclas_clicadas['w']:
            self.som_cursor.play()
            self.__opcao = (self.__opcao - 1) % len(self.__opcoes)
        elif teclas_clicadas['s']:
            self.som_cursor.play()
            self.__opcao = (self.__opcao + 1) % len(self.__opcoes)

        self.__cursor_rect.midtop = (
                    self.__distancia_cursor, self.__opcoes[self.__opcao][1])
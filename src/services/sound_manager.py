from Singleton import Singleton
import pygame
import os


class GerenciadorSons(metaclass=Singleton):
    def __init__(self):
        pygame.mixer.init()
        self.__local_sons = {
            'sons': { 
                'apertou_botao': 'apertou_botao.wav',
                'colisao': 'colisao.wav',
                'item': 'item.wav',
                'mudando_cursor': 'mudando_cursor.wav',
                'game_over': 'game_over.wav'
            }
        }
        self.__sons_carregados = None
        self.__carregarSons()

    def __carregarSons(self):
        sons = {}
        for componente, som in self.__local_sons.items():
            sons[componente] = {}
            for descricao, som in som.items():
                sons[componente][descricao] = pygame.mixer.Sound(
                    os.path.join('versao_final', 'sons', som))


        self.__sons_carregados = sons

    def getSound(self, componente: str, descricao: str) -> pygame.mixer.Sound:
        som = self.__sons_carregados[componente][descricao]
        return som


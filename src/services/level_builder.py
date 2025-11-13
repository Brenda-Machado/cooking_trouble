from Biblioteca import Biblioteca
from src.models.Fase import Fase
from src.utils.Coordenada import Coordenada
from src.models.entities.player import Jogador
from random import randrange
from InimigoObstaculo import InimigoObstaculo
from InimigoPessoa import InimigoPessoa
from src.models.entities.delivery_point import PontoEntrega
from Singleton import Singleton
from math import ceil
from copy import deepcopy


class ConstrutorFase(metaclass=Singleton):
    def __init__(self):
        self.__biblioteca = Biblioteca()

    # METODO
    def constroiFase(self, nivel: str, dificuldade: int) -> Fase:
        mapa = self.__biblioteca.getMapaNivel(nivel)

        jogador = Jogador(Coordenada(mapa.spawn_jogador.x,mapa.spawn_jogador.y),
                          self.__biblioteca.getSprites(nivel)['jogador'])
        # dificuldade de 1 a 3
        num_inimigos_p = ceil((dificuldade+1)/3 * len(mapa.spawn_inimigos_p))
        num_inimigos_o = ceil((dificuldade+1)/3 * len(mapa.caminho_inimigos_o))

        lista_spawn_p = mapa.spawn_inimigos_p
        lista_caminhos_o = mapa.caminho_inimigos_o
        inimigos_pessoa, inimigos_obstaculo = [], []
        for i in range(num_inimigos_p):
            coord = lista_spawn_p.pop(randrange(len(lista_spawn_p)))
            inimigos_pessoa.append(InimigoPessoa(Coordenada(coord.x, coord.y), sprites=self.__biblioteca.getSprites(nivel)['inimigo_pessoa']))  # adiciona um inimigo de um spawn aleatorio
        for i in range(num_inimigos_o):
            caminho = lista_caminhos_o.pop(randrange(len(lista_caminhos_o)))
            inimigos_obstaculo.append(InimigoObstaculo(deepcopy(caminho), sprites=self.__biblioteca.getSprites(nivel)['inimigo_obstaculo']))

        pontos_entrega = []
        for pe in mapa.pontos_entrega:
            pontos_entrega.append(PontoEntrega(pe))

        num_itens = 1 + dificuldade * 2
        itens_diferentes = len(
            self.__biblioteca.getItensDificuldade(dificuldade, nivel))
        lista_itens = []
        for i in range(num_itens):
            lista_itens.append(self.__biblioteca.getItensDificuldade(
                dificuldade, nivel)[randrange(itens_diferentes)])

        return Fase(jogador, inimigos_pessoa, inimigos_obstaculo, mapa, pontos_entrega, lista_itens)

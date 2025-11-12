import pygame
from src.models.entities.base.Movel import Movel
from src.utils.Coordenada import Coordenada
from src.utils.Tamanho import Tamanho
from GerenciadorImagens import GerenciadorImagens


class InimigoPessoa(Movel):
    def __init__(self, spawn: Coordenada, raio_deslocamento: float = 20, raio_deteccao: float = 300, velocidade: float = 3, sprites: list = []):
        super().__init__(Coordenada(spawn.x, spawn.y), Tamanho(55, 55), velocidade, sprites)
        self.__spawn = spawn
        self.__raio_deslocamento = raio_deslocamento
        self.__raio_deteccao = raio_deteccao
        self.__imagem_atual = None
        

    # praticamente um versor da direcao de deslocamento
    def decideDirecao(self, coord_jogador: Coordenada):
        if self.atingido == 0:
            if(coord_jogador != None and self.coord.calculaDistancia(coord_jogador) <= self.__raio_deteccao):
                self.direcao_deslocamento = Coordenada.versorEntreCoordenadas(
                    self.coord, coord_jogador)
            elif(self.coord.calculaDistancia(self.__spawn) > self.__raio_deslocamento):
                self.direcao_deslocamento = Coordenada.versorEntreCoordenadas(
                    self.coord, self.__spawn)
            else:
                self.direcao_deslocamento = Coordenada(0, 0)

        else:
            self.direcao_deslocamento = Coordenada.versorEntreCoordenadas(
                self.coord_atingido, self.coord)

    def colidiu(self, coord: Coordenada):
        self.atingido = 30
        self.coord_atingido = coord

    def desenhar(self, posicao_camera):
        if self.atingido:
            imagem = self.imagens[len(self.imagens)-2]
            if self.angulo >= 180:
                imagem = self.imagens[len(self.imagens)-1]
        elif self.direcao_deslocamento.x == 0 and self.direcao_deslocamento.y == 0:
            if self.angulo < 180:
                imagem = self.imagens[0]
            else:
                imagem = self.imagens[1]
        elif self.direcao_deslocamento.x < 0 or (self.direcao_deslocamento.x == 0 and self.direcao_deslocamento.y < 0):
            if self.__imagem_atual == self.imagens[2]:
                imagem = self.imagens[3]
            else:
                imagem = self.imagens[2]
        else:
            if self.__imagem_atual == self.imagens[4]:
                imagem = self.imagens[5]
            else:
                imagem = self.imagens[4]

        self.__imagem_atual = imagem
        return imagem, super().desenhar(posicao_camera)

    def salvar_imagens(self, sprites: list):
        lista = []
        for nome in sprites:
            lista.append(GerenciadorImagens().getSprite(
                'inimigo_pessoa', nome, self.tamanho.largura, self.tamanho.altura))
        return lista

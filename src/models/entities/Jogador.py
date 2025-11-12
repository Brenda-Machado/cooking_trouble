from src.models.entities.base.Movel import Movel
from src.utils.Coordenada import Coordenada
from src.utils.Tamanho import Tamanho
from src.models.entities.Item import Item
from src.models.entities.PontoEntrega import PontoEntrega
from GerenciadorImagens import GerenciadorImagens


class Jogador(Movel):
    def __init__(self, coord: Coordenada, sprites):
        super().__init__(coord, Tamanho(55, 55), 7, sprites=sprites)
        self.__item_carregado = None
        self.__imagem_atual = None

    @property
    def item_carregado(self) -> Item:
        return self.__item_carregado

    @item_carregado.setter
    def item_carregado(self, item):
        self.__item_carregado = item

    def pegarItem(self, item: Item) -> bool:
        if(item.ativo and self.coord.calculaDistancia(item.coord) <= item.raio_interacao):
            self.__item_carregado = item
            item.ativo = False
            return True
        else:
            return False

    def perderItem(self):
        self.__item_carregado.ativo = True
        self.__item_carregado = None

    def entregarItem(self, ponto_entrega: PontoEntrega) -> bool:
        if(self.item_carregado != None and self.coord.calculaDistancia(ponto_entrega.coord) <= ponto_entrega.raio_interacao):
            self.item_carregado = None
            return True
        else:
            return False

    def colidiu(self, coord: Coordenada):
        self.atingido = 30
        self.coord_atingido = coord
        if self.item_carregado != None:
            self.perderItem()

    def decideDirecao(self, cima: bool, baixo: bool, direita: bool, esquerda: bool):
        if self.atingido == 0:
            horizontal = 0
            vertical = 0
            if(cima):
                vertical -= 1
            if(baixo):
                vertical += 1
            if(direita):
                horizontal += 1
            if(esquerda):
                horizontal -= 1

            self.direcao_deslocamento = Coordenada.versorEntreCoordenadas(
                Coordenada(0, 0), Coordenada(horizontal, vertical))

        else:
            self.direcao_deslocamento = Coordenada.versorEntreCoordenadas(
                self.coord_atingido, self.coord)

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
                'jogador', nome, self.tamanho.largura, self.tamanho.altura))
        return lista

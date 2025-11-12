from Movel import Movel
from Coordenada import Coordenada
from Tamanho import Tamanho
from copy import deepcopy
from GerenciadorImagens import GerenciadorImagens


class InimigoObstaculo(Movel):
    def __init__(self, caminho: list, tamanho: Tamanho = Tamanho(100, 80), velocidade: float = 8, sprites: list = []):
        if(len(caminho) < 2):
            raise ValueError(
                f'Caminho em InimigoObstaculo: {self} eh muito pequeno (len(caminho) < 2)')
        super().__init__(caminho[0], tamanho, velocidade, sprites)
        self.__caminho = deepcopy(caminho)
        self.__proximo_ponto_caminho = 1

    def decideDirecao(self):  
        if(self.coord.calculaDistancia(self.__caminho[self.__proximo_ponto_caminho]) <= 0.05):
            self.__proximo_ponto_caminho = (
                self.__proximo_ponto_caminho + 1) % len(self.__caminho)
        else:
            direcao = Coordenada.versorEntreCoordenadas(
                self.coord, self.__caminho[self.__proximo_ponto_caminho])
            intensidade_velocidade = (self.coord.calculaDistancia(
                self.__caminho[self.__proximo_ponto_caminho]) / self.velocidade)
            if(intensidade_velocidade >= 1):
                intensidade_velocidade = 1
            self.direcao_deslocamento = Coordenada(
                direcao.x*intensidade_velocidade, direcao.y*intensidade_velocidade)

    def colidiu(self, coord: Coordenada):
        pass

    def salvar_imagens(self, sprites):
        lista = []
        for nome in sprites:
            lista.append(GerenciadorImagens().getSprite(
                'inimigo_obstaculo', nome, self.tamanho.largura, self.tamanho.altura))
        return lista

    def desenhar(self, posicao_camera):
        imagem = self.imagens[0]
        if self.angulo == 90:
            imagem = self.imagens[1]
        elif self.angulo == 180:
            imagem = self.imagens[2]
        elif self.angulo == 270:
            imagem = self.imagens[3]

        return imagem, super().desenhar(posicao_camera)

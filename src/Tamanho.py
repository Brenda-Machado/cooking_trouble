class Tamanho:
    def __init__(self, largura:int, altura:int):
        self.__altura = altura
        self.__largura = largura

    @property
    def altura(self) -> float:
        return self.__altura

    @property
    def largura(self) -> float:
        return self.__largura

    @altura.setter
    def altura(self, altura:float):
        self.__altura = altura

    @largura.setter
    def largura(self, largura:float):
        self.__largura = largura

from src.models.entities.Mapa import Mapa
from src.models.entities.item import Item
from src.utils.Coordenada import Coordenada
from ObstaculoMapa import ObstaculoMapa
from src.utils.Tamanho import Tamanho
from Singleton import Singleton


class Biblioteca(metaclass=Singleton):

    def __init__(self):
        self.__mapas = {
            # mapa mercado
            'mercado': Mapa(
                #tamanho
                Tamanho(2400, 1720),
                #spawn jogador
                Coordenada(220, 1520),
                #spawn inimigos p
                [
                    Coordenada(185, 875), Coordenada(860, 195), Coordenada(860, 875), Coordenada(1405, 875),
                    Coordenada(1800, 165), Coordenada(1800, 485), Coordenada(1800, 1245), Coordenada(1800, 1560)
                ],
                #caminhos inimigos o
                [
                    [Coordenada(320, 920), Coordenada(320, 1460), Coordenada(680, 1460), Coordenada(680, 920)],
                    [Coordenada(320, 260), Coordenada(320, 800), Coordenada(680, 800), Coordenada(680, 260)],
                    [Coordenada(1040, 140), Coordenada(1040, 520), Coordenada(1400, 520), Coordenada(1400, 140)],
                    [Coordenada(1040, 1200), Coordenada(1040, 1580), Coordenada(1400, 1580), Coordenada(1400, 1200)],
                    [Coordenada(1520, 800), Coordenada(1520, 920), Coordenada(2080, 920), Coordenada(2080, 800)],
                    [Coordenada(2160, 160), Coordenada(2160, 1560), Coordenada(2240, 1560), Coordenada(2240, 160)],
                    
                ],
                #spawn itens
                [
                    Coordenada(65, 535), Coordenada(545, 520), Coordenada(455, 1035), Coordenada(905, 1200),
                    Coordenada(1220, 65), Coordenada(1175, 715), Coordenada(1265, 1005), Coordenada(1220, 1295),
                    Coordenada(1220, 1505), Coordenada(1675, 65), Coordenada(1535, 300), Coordenada(2065, 300),
                    Coordenada(1595, 615), Coordenada(1975, 705), Coordenada(1800, 1015), Coordenada(1535, 1415),
                    Coordenada(1935, 1655), Coordenada(2335, 475), Coordenada(2335, 865), Coordenada(2335, 1625)
                ],
                #pontos entrega
                [
                    Coordenada(170, 1520)
                ],
                #obstaculos
                [
                    ObstaculoMapa(Coordenada(0, 0), Tamanho(2400, 80), 'tijolos_vermelhos_cima'),
                    ObstaculoMapa(Coordenada(0, 80), Tamanho(80, 1400), 'tijolos_vermelhos_esquerda'),
                    ObstaculoMapa(Coordenada(0, 1400), Tamanho(150, 240), 'caixa'),
                    ObstaculoMapa(Coordenada(440, 320), Tamanho(120, 400), 'mostruario_vertical_vazio'),
                    ObstaculoMapa(Coordenada(440, 1000), Tamanho(120, 400), 'mostruario_vertical_cheio'),
                    ObstaculoMapa(Coordenada(280, 1640), Tamanho(2120, 80), 'tijolos_vermelhos_baixo'),
                    ObstaculoMapa(Coordenada(800, 320), Tamanho(120, 400), 'balcao_vertical'),
                    ObstaculoMapa(Coordenada(800, 1000), Tamanho(120, 400), 'caixas_grandes'),
                    ObstaculoMapa(Coordenada(1160, 200), Tamanho(120, 240), 'placa_sale'),
                    ObstaculoMapa(Coordenada(1160, 600), Tamanho(120, 520), 'mostruario_vertical_cheio'),
                    ObstaculoMapa(Coordenada(1160, 1280), Tamanho(120, 240), 'prateleira_M_vazia'),
                    ObstaculoMapa(Coordenada(1520, 240), Tamanho(560, 120), 'prateleira_horizontal'),
                    ObstaculoMapa(Coordenada(1520, 600), Tamanho(560, 120), 'prateleira_M_cheia3'),
                    ObstaculoMapa(Coordenada(1520, 1000), Tamanho(560, 120), 'mostruario_G_cheio'),
                    ObstaculoMapa(Coordenada(1520, 1360), Tamanho(560, 120), 'prateleira_M_cheia2'),
                    ObstaculoMapa(Coordenada(2320, 80), Tamanho(80, 1560), 'tijolos_vermelhos_direita'),
                ], 'mercado'),
            # mapa cozinha
            'cozinha': Mapa(
                #tamanho
                Tamanho(2400, 1720),
                #spawn jogador
                Coordenada(1200, 185),
                #spawn inimigos p
                [
                    Coordenada(185, 465), Coordenada(225, 1495), Coordenada(905, 640), Coordenada(1200, 345),
                    Coordenada(1200, 1225), Coordenada(1465, 640), Coordenada(2215, 465), Coordenada(2175, 1495)
                ],
                #caminhos inimigos o
                [
                    [Coordenada(500, 500), Coordenada(500, 780), Coordenada(1060, 780), Coordenada(1060, 500)],
                    [Coordenada(560, 1060), Coordenada(560, 1180), Coordenada(1120, 1180), Coordenada(1120, 1060)],
                    [Coordenada(480, 1460), Coordenada(480, 1580), Coordenada(1040, 1580), Coordenada(1040, 1460)],
                    [Coordenada(1340, 500), Coordenada(1340, 780), Coordenada(1900, 780), Coordenada(1900, 500)],
                    [Coordenada(1280, 1060), Coordenada(1280, 1180), Coordenada(1840, 1180), Coordenada(1840, 1060)],
                    [Coordenada(1360, 1460), Coordenada(1360, 1580), Coordenada(1920, 1580), Coordenada(1920, 1460)],
                    
                ],
                #spawn itens
                [
                    Coordenada(65, 815), Coordenada(65, 860), Coordenada(65, 905),
                    Coordenada(375, 65), Coordenada(420, 65), Coordenada(465, 65),
                    Coordenada(1935, 65), Coordenada(1980, 65), Coordenada(2025, 65),
                    Coordenada(2335, 815), Coordenada(2335, 860), Coordenada(2335, 905)
                ],
                #pontos entrega
                [
                    Coordenada(330, 550), Coordenada(570, 640), Coordenada(450, 1180), Coordenada(720, 640),
                    Coordenada(840, 1280), Coordenada(1200, 560), Coordenada(1200, 900), Coordenada(1200, 1390),
                    Coordenada(1560, 1280), Coordenada(1670, 640), Coordenada(1780, 320), Coordenada(1840, 640),
                    Coordenada(2080, 1100)
                ],
                #obstaculos
                [
                    ObstaculoMapa(Coordenada(0, 0), Tamanho(2400, 80), 'tijolos_azuis_cima'),
                    ObstaculoMapa(Coordenada(0, 80), Tamanho(80, 1560), 'tijolos_azuis_esquerda'),
                    ObstaculoMapa(Coordenada(80, 760), Tamanho(80, 40), 'balcao_horizontal2'),
                    ObstaculoMapa(Coordenada(80, 920), Tamanho(80, 40), 'balcao_horizontal2'),
                    ObstaculoMapa(Coordenada(0, 1640), Tamanho(2400, 80), 'tijolos_azuis_baixo'),
                    ObstaculoMapa(Coordenada(320, 80), Tamanho(40, 80), 'balcao_vertical2'),
                    ObstaculoMapa(Coordenada(480, 80), Tamanho(40, 80), 'balcao_vertical2'),
                    ObstaculoMapa(Coordenada(320, 320), Tamanho(120, 440), 'balcao_vertical2'),
                    ObstaculoMapa(Coordenada(320, 960), Tamanho(120, 440), 'balcao_vertical2'),
                    ObstaculoMapa(Coordenada(440, 320), Tamanho(80, 120), 'fogao'),
                    ObstaculoMapa(Coordenada(520, 320), Tamanho(200, 120), 'balcao_p'),
                    ObstaculoMapa(Coordenada(720, 320), Tamanho(80, 120), 'geladeira'),
                    ObstaculoMapa(Coordenada(800, 320), Tamanho(200, 120), 'balcao_p'),
                    ObstaculoMapa(Coordenada(560, 560), Tamanho(120, 180), 'balcao_vertical2'),
                    ObstaculoMapa(Coordenada(600, 840), Tamanho(80, 120), 'utensilio'),
                    ObstaculoMapa(Coordenada(680, 840), Tamanho(160, 120), 'balcao_horizontal2'),
                    ObstaculoMapa(Coordenada(840, 840), Tamanho(80, 120), 'fogao'),
                    ObstaculoMapa(Coordenada(920, 840), Tamanho(200, 120),'balcao_p'),
                    ObstaculoMapa(Coordenada(680, 1280), Tamanho(1040, 120), 'balcao_horizontal2'),
                    ObstaculoMapa(Coordenada(1120, 560), Tamanho(120, 180), 'balcao_vertical2'),
                    ObstaculoMapa(Coordenada(1280, 840), Tamanho(200, 120), 'balcao_p'),
                    ObstaculoMapa(Coordenada(1480, 840), Tamanho(80, 120), 'geladeira'),
                    ObstaculoMapa(Coordenada(1560, 840), Tamanho(80, 120), 'utensilio'),
                    ObstaculoMapa(Coordenada(1640, 840), Tamanho(160, 120), 'balcao_horizontal2'),
                    ObstaculoMapa(Coordenada(1410, 320), Tamanho(80, 120), 'fogao'),
                    ObstaculoMapa(Coordenada(1490, 320), Tamanho(200, 120), 'balcao_p'),
                    ObstaculoMapa(Coordenada(1690, 320), Tamanho(80, 120), 'utensilio'),
                    ObstaculoMapa(Coordenada(1770, 320), Tamanho(80, 120), 'geladeira'),
                    ObstaculoMapa(Coordenada(1850, 320), Tamanho(120, 120), 'balcao_horizontal2'),
                    ObstaculoMapa(Coordenada(1680, 560), Tamanho(120, 180), 'balcao_vertical2'),
                    ObstaculoMapa(Coordenada(1880, 80), Tamanho(40, 80), 'balcao_vertical2'),
                    ObstaculoMapa(Coordenada(2040, 80), Tamanho(40, 80), 'balcao_vertical2'),
                    ObstaculoMapa(Coordenada(1960, 320), Tamanho(120, 440), 'balcao_vertical2'),
                    ObstaculoMapa(Coordenada(1960, 960), Tamanho(120, 440), 'balcao_vertical2'),
                    ObstaculoMapa(Coordenada(2240, 760), Tamanho(80, 40), 'balcao_horizontal2'),
                    ObstaculoMapa(Coordenada(2240, 920), Tamanho(80, 40), 'balcao_horizontal2'),
                    ObstaculoMapa(Coordenada(2320, 80), Tamanho(80, 1560), 'tijolos_azuis_direita')
                ], 'cozinha'),
            # mapa restaurante
            'restaurante': Mapa(
                #tamanho
                Tamanho(2400, 1720),
                #spawn jogador
                Coordenada(2200, 400),
                #spawn inimigos p
                [
                    Coordenada(195, 145), Coordenada(185, 1325), Coordenada(945, 425), Coordenada(945, 815),
                    Coordenada(1405, 605), Coordenada(1800, 725), Coordenada(1765, 1160), Coordenada(1765, 1545)
                ],
                #caminhos inimigos o
                [
                    [Coordenada(560, 360), Coordenada(560, 850), Coordenada(240, 850), Coordenada(240, 360)],
                    [Coordenada(280, 1310), Coordenada(280, 1430), Coordenada(840, 1430), Coordenada(840, 1310)],
                    [Coordenada(1080, 360), Coordenada(1080, 1200), Coordenada(1320, 1200), Coordenada(1320, 360)],
                    [Coordenada(1400, 800), Coordenada(1400, 800), Coordenada(2040, 800), Coordenada(2040, 800)],
                    [Coordenada(1400, 360), Coordenada(1400, 360), Coordenada(2040, 360), Coordenada(2040, 360)],
                    [Coordenada(1400, 940), Coordenada(1400, 940), Coordenada(2040, 940), Coordenada(2040, 940)],
                    
                ],
                #spawn itens
                [
                    Coordenada(120, 1290), Coordenada(2300, 400), Coordenada(2300, 400),
                    Coordenada(120, 1290), Coordenada(2300, 1290)
                ],
                #pontos entrega
                [
                    Coordenada(335, 200), Coordenada(1135, 1520), Coordenada(1535, 1520),
                    Coordenada(735, 520), Coordenada(1535, 200), Coordenada(1935, 1520),
                    Coordenada(335, 900), Coordenada(735, 900), Coordenada(1535, 800),
                    Coordenada(335, 1120), Coordenada(735, 1120), Coordenada(1935, 200), Coordenada(1935, 600),
                    Coordenada(335, 1520), Coordenada(735, 1520)
                ],
                #obstaculos
                [
                    ObstaculoMapa(Coordenada(0, 0), Tamanho(2400, 140), 'parede_janelas'),
                    ObstaculoMapa(Coordenada(0, 80), Tamanho(80, 1560), 'mapa_laterais_esquerda'),
                    ObstaculoMapa(Coordenada(0, 1640), Tamanho(2400, 80), 'mapa_laterais_baixo'),
                    ObstaculoMapa(Coordenada(280, 160), Tamanho(60, 100), 'cliente_sentado1_direita'),
                    ObstaculoMapa(Coordenada(455, 160), Tamanho(60, 100), 'cliente_sentado4_esquerda'),
                    ObstaculoMapa(Coordenada(335, 160), Tamanho(120, 120), 'mesa'),
                    ObstaculoMapa(Coordenada(300, 520), Tamanho(40, 80), 'cadeira_direita'),
                    ObstaculoMapa(Coordenada(455, 520), Tamanho(40, 80), 'cadeira_esquerda'),
                    ObstaculoMapa(Coordenada(335, 520), Tamanho(120, 120), 'mesa'),
                    ObstaculoMapa(Coordenada(700, 160), Tamanho(40, 80), 'cadeira_direita'),
                    ObstaculoMapa(Coordenada(855, 160), Tamanho(40, 80), 'cadeira_esquerda'),
                    ObstaculoMapa(Coordenada(735, 160), Tamanho(120, 120), 'mesa'),
                    ObstaculoMapa(Coordenada(680, 520), Tamanho(60, 100), 'cliente_sentado4_direita'),
                    ObstaculoMapa(Coordenada(855, 520), Tamanho(40, 80), 'cadeira_esquerda'),
                    ObstaculoMapa(Coordenada(735, 520), Tamanho(120, 120), 'mesa'),
                    ObstaculoMapa(Coordenada(280, 980), Tamanho(60, 100), 'cliente_sentado2_direita'),
                    ObstaculoMapa(Coordenada(455, 980), Tamanho(60, 100), 'cliente_sentado3_esquerda'),
                    ObstaculoMapa(Coordenada(335, 980), Tamanho(120, 120), 'mesa'),
                    ObstaculoMapa(Coordenada(680, 980), Tamanho(60, 100), 'cliente_sentado3_direita'),
                    ObstaculoMapa(Coordenada(855, 980), Tamanho(40, 80), 'cadeira_esquerda'),
                    ObstaculoMapa(Coordenada(735, 980), Tamanho(120, 120), 'mesa'),
                    ObstaculoMapa(Coordenada(240, 1080), Tamanho(680, 40), 'mapa_laterais_deitado'),
                    ObstaculoMapa(Coordenada(280, 1120), Tamanho(60, 100), 'cliente_sentado3_direita'),
                    ObstaculoMapa(Coordenada(455, 1120), Tamanho(60, 100), 'cliente_sentado4_esquerda'),
                    ObstaculoMapa(Coordenada(335, 1120), Tamanho(120, 120), 'mesa'),
                    ObstaculoMapa(Coordenada(680, 1120), Tamanho(60, 100), 'cliente_sentado2_direita'),
                    ObstaculoMapa(Coordenada(855, 1120), Tamanho(60, 100), 'cliente_sentado1_esquerda'),
                    ObstaculoMapa(Coordenada(735, 1120), Tamanho(120, 120), 'mesa'),
                    ObstaculoMapa(Coordenada(280, 1520), Tamanho(60, 100), 'cliente_sentado4_direita'),
                    ObstaculoMapa(Coordenada(455, 1520), Tamanho(40, 80), 'cadeira_esquerda'),
                    ObstaculoMapa(Coordenada(335, 1520), Tamanho(120, 120), 'mesa'),
                    ObstaculoMapa(Coordenada(700, 1520), Tamanho(40, 80), 'cadeira_direita'),
                    ObstaculoMapa(Coordenada(855, 1520), Tamanho(60, 100), 'cliente_sentado2_esquerda'),
                    ObstaculoMapa(Coordenada(735, 1520), Tamanho(120, 120), 'mesa'),
                    ObstaculoMapa(Coordenada(1080, 1520), Tamanho(60, 100), 'cliente_sentado1_direita'),
                    ObstaculoMapa(Coordenada(1255, 1520), Tamanho(60, 100), 'cliente_sentado3_esquerda'),
                    ObstaculoMapa(Coordenada(1135, 1520), Tamanho(120, 120), 'mesa'),
                    ObstaculoMapa(Coordenada(1500, 1520), Tamanho(40, 80), 'cadeira_direita'),
                    ObstaculoMapa(Coordenada(1655, 1520), Tamanho(60, 100), 'cliente_sentado3_esquerda'),
                    ObstaculoMapa(Coordenada(1535, 1520), Tamanho(120, 120), 'mesa'),
                    ObstaculoMapa(Coordenada(1500, 1120), Tamanho(40, 80), 'cadeira_direita'),
                    ObstaculoMapa(Coordenada(1655, 1120), Tamanho(40, 80), 'cadeira_esquerda'),
                    ObstaculoMapa(Coordenada(1535, 1120), Tamanho(120, 120), 'mesa'),
                    ObstaculoMapa(Coordenada(1500, 600), Tamanho(40, 80), 'cadeira_direita'),
                    ObstaculoMapa(Coordenada(1655, 600), Tamanho(40, 80), 'cadeira_esquerda'),
                    ObstaculoMapa(Coordenada(1535, 600), Tamanho(120, 120), 'mesa'),
                    ObstaculoMapa(Coordenada(1535, 540), Tamanho(520, 40), 'mapa_laterais_deitado'),
                    ObstaculoMapa(Coordenada(1480, 160), Tamanho(60, 100), 'cliente_sentado1_direita'),
                    ObstaculoMapa(Coordenada(1655, 160), Tamanho(60, 100), 'cliente_sentado2_esquerda'),
                    ObstaculoMapa(Coordenada(1535, 160), Tamanho(120, 120), 'mesa'),
                    ObstaculoMapa(Coordenada(1880, 160), Tamanho(60, 100), 'cliente_sentado4_direita'),
                    ObstaculoMapa(Coordenada(2055, 160), Tamanho(60, 100), 'cliente_sentado3_esquerda'),
                    ObstaculoMapa(Coordenada(1935, 160), Tamanho(120, 120), 'mesa'),
                    ObstaculoMapa(Coordenada(1900, 1120), Tamanho(40, 80), 'cadeira_direita'),
                    ObstaculoMapa(Coordenada(2055, 1120), Tamanho(40, 80), 'cadeira_esquerda'),
                    ObstaculoMapa(Coordenada(1935, 1120), Tamanho(120, 120), 'mesa'),
                    ObstaculoMapa(Coordenada(1880, 600), Tamanho(60, 100), 'cliente_sentado1_direita'),
                    ObstaculoMapa(Coordenada(2055, 600), Tamanho(40, 80), 'cadeira_esquerda'),
                    ObstaculoMapa(Coordenada(1935, 600), Tamanho(120, 120), 'mesa'),
                    ObstaculoMapa(Coordenada(1900, 1520), Tamanho(40, 80), 'cadeira_direita'),
                    ObstaculoMapa(Coordenada(2055, 1520), Tamanho(40, 80), 'cadeira_esquerda'),
                    ObstaculoMapa(Coordenada(1935, 1520), Tamanho(120, 120), 'mesa'),
                    ObstaculoMapa(Coordenada(1160, 440), Tamanho(80, 680), 'mapa_laterais_divisao'),
                    ObstaculoMapa(Coordenada(2320, 80), Tamanho(80, 1560), 'mapa_laterais_direita')
                ], 'restaurante')
        }
        self.__lista_itens = [
            #dificuldade 0
            {'mercado': [Item('Ovo'), Item('Queijo'), Item('Presunto')],
             'cozinha':[Item('Ovo'), Item('Queijo'), Item('Presunto')],
             'restaurante':[Item('Omelete')]},
            #dificuldade 1
            {'mercado': [Item('Massa'), Item('Molho de tomate'), Item('Carne Moida')],
             'cozinha':[Item('Massa'), Item('Molho de tomate'), Item('Carne Moida')],
             'restaurante':[Item('Macarronada'), Item('Lasanha')]},
            #dificuldade 2
            {'mercado': [Item('Arroz'), Item('Feijao'), Item('Carne de porco')],
             'cozinha':[Item('Arroz'), Item('Feijao'), Item('Carne de porco')],
             'restaurante':[Item('Feijoada'), Item('PF')]}
        ]

        self.__sprites = {
            'mercado': {
                'jogador': ['parado_esquerda', 'parado_direita', 'andando1_esquerda', 'andando2_esquerda', 
                            'andando1_direita', 'andando2_direita', 'atingido_esquerda', 'atingido_direita'],
                'inimigo_obstaculo': ['carrinho_frente/tras', 'carrinho_esquerda', 'carrinho_frente/tras', 'carrinho_direita'],
                'inimigo_pessoa': ['parado_esquerda', 'parado_direita', 'andando1_esquerda', 'andando2_esquerda', 
                            'andando1_direita', 'andando2_direita', 'atingido_esquerda', 'atingido_direita']
            },
            'cozinha':{
                'jogador': ['parado_esquerda', 'parado_direita', 'andando1_esquerda', 'andando2_esquerda', 
                            'andando1_direita', 'andando2_direita', 'atingido_esquerda', 'atingido_direita'],
                'inimigo_obstaculo': ['carrinho_limpeza_tras', 'carrinho_limpeza_esquerda', 'carrinho_limpeza_frente', 'carrinho_limpeza_direita'],
                'inimigo_pessoa': ['parado_esquerda', 'parado_direita', 'andando1_esquerda', 'andando2_esquerda', 
                            'andando1_direita', 'andando2_direita', 'atingido_esquerda', 'atingido_direita']
            },
            'restaurante':{
                'jogador': ['parado_esquerda', 'parado_direita', 'andando1_esquerda', 'andando2_esquerda', 
                            'andando1_direita', 'andando2_direita', 'atingido_esquerda', 'atingido_direita'],
                'inimigo_obstaculo': ['carrinho_comida_tras', 'carrinho_comida_esquerda', 'carrinho_comida_frente', 'carrinho_comida_direita'],
                'inimigo_pessoa': ['parado_esquerda', 'parado_direita', 'andando1_esquerda', 'andando2_esquerda', 
                            'andando1_direita', 'andando2_direita', 'atingido_esquerda', 'atingido_direita']
            }
        }

    def getMapaNivel(self, nivel: str) -> Mapa:
        return self.__mapas[nivel]

    def getItensDificuldade(self, dificuldade: int, nivel: str):
        return [*self.__lista_itens[dificuldade][nivel]]

    def getSprites(self, nivel: str):
        return self.__sprites[nivel]

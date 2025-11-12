from Singleton import Singleton
import pygame
import os


class GerenciadorImagens(metaclass=Singleton):
    def __init__(self):
        self.__local_imagens = {
            # diretorio de referencia: versao_final/sprites (colocar as imagens/pastas dentro)
            'jogador': {
                'parado_esquerda': 'Jogador/jogador_parado_esquerda.png',
                'parado_direita': 'Jogador/jogador_parado.png',
                'andando1_esquerda': 'Jogador/jogador_andando1_esquerda.png',
                'andando2_esquerda': 'Jogador/jogador_andando2_esquerda.png',
                'andando1_direita': 'Jogador/jogador_andando1_direita.png',
                'andando2_direita': 'Jogador/jogador_andando2_direita.png',
                'atingido_esquerda': 'Jogador/jogador_atingido_esquerda.png',
                'atingido_direita': 'Jogador/jogador_atingido_direita.png'
            },
            'mapa': {
                'mercado': 'Supermercado/Mapa_supermercado.png',
                'cozinha': 'Cozinha/Mapa_cozinha.jpeg',
                'restaurante': 'Restaurante/mapa_piso.png'
            },
            'obstaculo': {
                # mercado
                'balcao_vertical': 'Supermercado/balcao_comprido.png',
                'balcao_horizontal': 'Supermercado/balcao_deitado.png',
                'balcao_grande_comida': 'Supermercado/balcao_grande_cheio.png',
                'caixa': 'Supermercado/caixa_grande.png',
                'caixas_grandes': 'Supermercado/caixas_grandes.png',
                'mostruario_vertical_vazio': 'Supermercado/mostruario_comprido_vazio.png',
                'mostruario_vertical_cheio': 'Supermercado/mostruario_comprido.png',
                'mostruario_G_cheio': 'Supermercado/mostruario_grande_cheio.png',
                'mostruario_G_vazio': 'Supermercado/mostruario_grande_vazio.png',
                'placa_sale': 'Supermercado/placa_sale.png',
                'prateleira_horizontal': 'Supermercado/prateleira_deitada.png',
                'prateleira_M_cheia1': 'Supermercado/prateleira_cortada.png',
                'prateleira_M_vazia': 'Supermercado/prateleira_grande_vazia.png',
                'prateleira_M_cheia2': 'Supermercado/prateleira_media_cheia1.png',
                'prateleira_M_cheia3': 'Supermercado/prateleira_media_cheia2.png',
                'tijolos_vermelhos_cima': 'Supermercado/tijolos_vermelhos_cima.png',
                'tijolos_vermelhos_baixo': 'Supermercado/tijolos_vermelhos_baixo.png',
                'tijolos_vermelhos_esquerda': 'Supermercado/tijolos_vermelhos_esquerda.png',
                'tijolos_vermelhos_direita': 'Supermercado/tijolos_vermelhos_direita.png',

                # cozinha
                'balcao_vertical2': 'Cozinha/Balcao_comprido_vazio.png',
                'balcao_horizontal2': 'Cozinha/Balcao_m_vazio.png',
                'balcao_grande_cozinha': 'Cozinha/Balcao_G_cheio.png',
                'balcao_p': 'Cozinha/Balcao_p.png',
                'fogao': 'Cozinha/Fogao.png',
                'utensilio': 'Cozinha/Balcao_p_utensilio.png',
                'geladeira': 'Cozinha/Geladeira.png',
                'tijolos_azuis_baixo': 'Cozinha/tijolinhos_azuis_baixo.png',
                'tijolos_azuis_direita': 'Cozinha/tijolinhos_azuis_direita.png',
                'tijolos_azuis_esquerda': 'Cozinha/tijolinhos_azuis_esquerda.png',
                'tijolos_azuis_cima': 'Cozinha/tijolos_azuis_cima.png',
                
                # restaurante
                'cadeira_direita': 'Restaurante/cadeira_direita.png',
                'cadeira_esquerda': 'Restaurante/cadeira_esquerda.png',
                'cliente_sentado1_direita': 'Restaurante/cliente_sentado1_direita.png',
                'cliente_sentado1_esquerda': 'Restaurante/cliente_sentado1_esquerda.png',
                'cliente_sentado2_direita': 'Restaurante/cliente_sentado2_direita.png',
                'cliente_sentado2_esquerda': 'Restaurante/cliente_sentado2_esquerda.png',
                'cliente_sentado3_direita': 'Restaurante/cliente_sentado3_direita.png',
                'cliente_sentado3_esquerda': 'Restaurante/cliente_sentado3_esquerda.png',
                'cliente_sentado4_direita': 'Restaurante/cliente_sentado4_direita.png',
                'cliente_sentado4_esquerda': 'Restaurante/cliente_sentado4_esquerda.png',
                'mapa_laterais_baixo': 'Restaurante/mapa_laterais_baixo.png',
                'mapa_laterais_direita': 'Restaurante/mapa_laterais_direita.png',
                'mapa_laterais_divisao': 'Restaurante/mapa_laterais_divisao.png',
                'mapa_laterais_deitado': 'Restaurante/mapa_laterais_deitado.png',
                'mapa_laterais_esquerda': 'Restaurante/mapa_laterais_esquerda.png',
                'mesa': 'Restaurante/mesa.png',
                'parede_janelas': 'Restaurante/parede_janelas.png',
                'planta': 'Restaurante/planta.png',
            },
            'item': {
                'Ovo': 'Itens/ovo.png',
                'Queijo': 'Itens/queijo.png',
                'Presunto': 'Itens/presunto.png',
                'Omelete': 'Itens/omelete.png',
                'Massa': 'Itens/massa.png',
                'Molho de tomate': 'Itens/tomate.png',
                'Carne Moida': 'Itens/carne_crua.png',
                'Macarronada': 'Itens/macarronada.png',
                'Lasanha': 'Itens/lasanha.png',
                'Arroz': 'Itens/pacote_arroz.png',
                'Feijao': 'Itens/feijao.png',
                'Carne de porco': 'Itens/carne_crua.png',
                'Feijoada': 'Itens/feijoada.png',
                'PF': 'Itens/feijoada.png'
            },
            'inimigo_obstaculo': {
                # mercado
                'carrinho_direita': 'Supermercado/Carrinho_direita.png',
                'carrinho_esquerda': 'Supermercado/Carrinho_esquerda.png',
                'carrinho_frente/tras': 'Supermercado/Carrinho_frente_e_tras.png',
                # cozinha
                'carrinho_limpeza_frente': 'Cozinha/Carrinho_limpeza_frente.png',
                'carrinho_limpeza_tras': 'Cozinha/Carrinho_limpeza_tras.png',
                'carrinho_limpeza_direita': 'Cozinha/Carrinho_limpeza_direita.png',
                'carrinho_limpeza_esquerda': 'Cozinha/Carrinho_limpeza_esquerda.png',
                # restaurante
                'carrinho_comida_frente': 'Restaurante/carrinho_comida_frente.png',
                'carrinho_comida_tras': 'Restaurante/carrinho_comida_tras.png',
                'carrinho_comida_direita': 'Restaurante/carrinho_comida_direita.png',
                'carrinho_comida_esquerda': 'Restaurante/carrinho_comida_esquerda.png',
            },
            'inimigo_pessoa': {
                'parado_esquerda': 'Inimigo/inimigo_parado_esquerda.png',
                'parado_direita': 'Inimigo/inimigo_parado_direita.png',
                'andando1_esquerda': 'Inimigo/inimigo_andando1_esquerda.png',
                'andando2_esquerda': 'Inimigo/inimigo_andando2_esquerda.png',
                'andando1_direita': 'Inimigo/inimigo_andando1_direita.png',
                'andando2_direita': 'Inimigo/inimigo_andando2_direita.png',
                'atingido_esquerda': 'Inimigo/inimigo_atingido_esquerda.png',
                'atingido_direita': 'Inimigo/inimigo_atingido_direita.png'
            },
            'fundo_menu': {'fundo_menu' : 'fundo_menu.png'}
        }
        self.__imagens_carregadas = None
        self.__carregarImagens()

    # vai gerar um dicionario com a mesma hierarquia que o self.__local_imagens, só que com as imagens carregadas
    def __carregarImagens(self):
        imagens = {}
        for componente, sprites in self.__local_imagens.items():
            imagens[componente] = {}
            for descricao, sprite in sprites.items():
                imagens[componente][descricao] = pygame.image.load(
                    os.path.join('versao_final', 'sprites', sprite))
                # deixa as imagens PNG transparentes
                imagens[componente][descricao].convert_alpha()

        self.__imagens_carregadas = imagens

    def getSprite(self, componente: str, descricao: str, largura: int, altura: int) -> pygame.image:
        imagem = pygame.transform.scale(
            self.__imagens_carregadas[componente][descricao], (largura, altura))
        return imagem


import pygame
import time
from pygame.locals import *
from src.models.Fase import Fase
from src.level_builder import ConstrutorFase
from InimigoPessoa import InimigoPessoa
from src.models.entities.player import Jogador
from src.models.entities.item import Item
from src.models.entities.delivery_point import PontoEntrega
#from Menu import Menu
from src.credits_menu import MenuCreditos
from src.main_menu import MenuPrincipal
from src.tutorial_menu import MenuTutorial
from Camera import Camera
from src.models.Estados import Estados
from GerenciadorImagens import GerenciadorImagens
from src.defeat_menu import MenuDerrota
from src.views.RenderizadorJogo import RenderizadorJogo
from src.victory_menu import MenuVitoria
from src.pause_manu import MenuPausa
from src.difficulty_menu import MenuDificuldade
from GerenciadorSons import GerenciadorSons


class ControladorJogo:

    def __init__(self):
        self.__rodando = True
        self.__display = None
        self.__tamanho_display = self.__largura, self.__altura = 720*2, 400*2
        self.__fase = None
        self.__nivel_atual = None
        self.__dificuldade = None
        self.__teclas_pressionadas = {  # True enquanto pressionadas
            'w': False, 'a': False, 's': False, 'd': False, 'espaco': False, 'esc': False, 'backspace': False, 'enter': False}
        self.__teclas_clicadas = {  # True somente por 1 frame quando soltas
            'w': False, 'a': False, 's': False, 'd': False, 'espaco': False, 'esc': False, 'backspace': False, 'enter': False}
        self.__timer_sec = 60
        self.__timer = None
        self.__fps = 60
        self.__timer_fps = pygame.time.Clock()
        self.__menu_prin = MenuPrincipal(self.__tamanho_display)
        self.__menu_crd = MenuCreditos(self.__tamanho_display)
        self.__menu_tut = MenuTutorial(self.__tamanho_display)
        self.__menu_derr = MenuDerrota(self.__tamanho_display)
        self.__menu_vit = MenuVitoria(self.__tamanho_display)
        self.__menu_pausa = MenuPausa(self.__tamanho_display)
        self.__menu_dif = MenuDificuldade(self.__tamanho_display)
        self.__render_jogo = RenderizadorJogo(self.__tamanho_display)
        self.__estado = Estados(1)  # menu principal
        self.__camera = None
        self.__som_botao = GerenciadorSons().getSound('sons', 'apertou_botao')
        self.__som_game_over = GerenciadorSons().getSound('sons', 'game_over')

    # GETTERS

    @property
    def fase(self):
        return self.__fase

    @property
    def nivel_atual(self):
        return self.__nivel_atual

    @property
    def dificuldade(self):
        return self.__dificuldade

    @property
    def tamanho_display(self):
        return self.__tamanho_display

    @property
    def altura(self):
        return self.__altura

    @property
    def largura(self):
        return self.__largura

    # LOOP

    def inicializar(self):
        pygame.init()
        self.__display = pygame.display.set_mode(
            self.tamanho_display, pygame.HWSURFACE)
        self.__rodando = True
        self.__timer = pygame.USEREVENT + 1

    def eventos(self, evento):
        if evento.type == pygame.QUIT:
            self.__rodando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_w:
                self.__teclas_pressionadas['w'] = True
                self.__teclas_clicadas['w'] = True
            elif evento.key == pygame.K_a:
                self.__teclas_pressionadas['a'] = True
                self.__teclas_clicadas['a'] = True
            elif evento.key == pygame.K_s:
                self.__teclas_pressionadas['s'] = True
                self.__teclas_clicadas['s'] = True
            elif evento.key == pygame.K_d:
                self.__teclas_pressionadas['d'] = True
                self.__teclas_clicadas['d'] = True
            elif evento.key == pygame.K_SPACE:
                self.__teclas_pressionadas['espaco'] = True
                self.__teclas_clicadas['espaco'] = True
            elif evento.key == pygame.K_ESCAPE:
                self.__teclas_pressionadas['esc'] = True
                self.__teclas_clicadas['esc'] = True
            elif evento.key == pygame.K_BACKSPACE:
                self.__teclas_pressionadas['backspace'] = True
                self.__teclas_clicadas['backspace'] = True
            elif evento.key == pygame.K_RETURN:
                self.__teclas_pressionadas['enter'] = True
                self.__teclas_clicadas['enter'] = True

        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_w:
                self.__teclas_pressionadas['w'] = False
            elif evento.key == pygame.K_a:
                self.__teclas_pressionadas['a'] = False
            elif evento.key == pygame.K_s:
                self.__teclas_pressionadas['s'] = False
            elif evento.key == pygame.K_d:
                self.__teclas_pressionadas['d'] = False
            elif evento.key == pygame.K_SPACE:
                self.__teclas_pressionadas['espaco'] = False
            elif evento.key == pygame.K_ESCAPE:
                self.__teclas_pressionadas['esc'] = False
            elif evento.key == pygame.K_BACKSPACE:
                self.__teclas_pressionadas['backspace'] = False
            elif evento.key == pygame.K_RETURN:
                self.__teclas_pressionadas['enter'] = False

        # se for do timer e se estiver jogando
        elif evento.type == self.__timer and int(self.__estado) == 0:
            if self.__timer_sec >= 0:
                self.__timer_sec -= 1

    def loop(self):
        self.MudaEstados()

        if self.__estado == 0:  # jogando
            self.__fase.movimento(self.__teclas_pressionadas)
            self.__fase.gerenciamentoItem(self.__teclas_pressionadas['espaco'])
            self.__fase.colisao_moveis()
            self.__camera.moverCamera()

        elif self.__estado == 1:  # principal
            self.__menu_prin.move_cursor(self.__teclas_clicadas)

        elif self.__estado == 2:  # dificuldade
            self.__menu_dif.move_cursor(self.__teclas_clicadas)

        elif self.__estado == 7:  # pause
            pass

        if True in self.__teclas_clicadas.values():
            for k in self.__teclas_clicadas.keys():
                self.__teclas_clicadas[k] = False

    def renderizar(self):
        if self.__estado == 0:  # jogando
            # renderizar jogo
            self.__render_jogo.renderizar(
                self.__display, self.__camera.posicao_int, self.__fase.mapa, self.__fase.ponto_entrega_ativo,
                self.__fase.inimigos_obstaculo, self.__fase.inimigos_pessoa, self.__fase.jogador,
                self.__fase.item_ativo, self.__timer_sec)
            # renderizar interface

        elif self.__estado == 1:  # principal
            self.__menu_prin.display_menu()

        elif self.__estado == 2:  # dificuldade
            # menu dificuldade
            self.__menu_dif.display_menu()

        elif self.__estado == 3:  # tutorial
            self.__menu_tut.display_menu()

        elif self.__estado == 4:  # creditos
            self.__menu_crd.display_menu()

        elif self.__estado == 5:  # vitoria
            self.__menu_vit.display_menu()

        elif self.__estado == 6:  # derrota
            self.__menu_derr.display_menu()
            self.__som_game_over.set_volume(0.3)
            self.__som_game_over.play()

        elif self.__estado == 7:  # pause
            # rederizar jogo um pouco mais escuro
            self.__render_jogo.renderizar(
                self.__display, self.__camera.posicao_int, self.__fase.mapa, self.__fase.ponto_entrega_ativo,
                self.__fase.inimigos_obstaculo, self.__fase.inimigos_pessoa, self.__fase.jogador,
                self.__fase.item_ativo, self.__timer_sec)
            self.__menu_pausa.display_menu()
            # renderizar menu de pause

        pygame.display.flip()

    def limpar(self):
        pygame.quit()

    def executar(self):
        if self.inicializar() == False:
            self.__rodando = False

        while self.__rodando:
            for evento in pygame.event.get():
                self.eventos(evento)
            self.loop()
            self.renderizar()
            self.__timer_fps.tick(self.__fps)
        self.limpar()

    # CONTROLADOR
    def novaFase(self):
        self.decide_fase()
        self.__fase = ConstrutorFase().constroiFase(
            self.__nivel_atual, self.__dificuldade)
        self.reiniciaTimer()
        self.__camera = Camera(self.__fase.jogador.rect, self.tamanho_display)
        print(self.__nivel_atual)

    def decide_fase(self):
        if self.__estado == 6:  # derrota
            pass  # continua igual
        elif self.__estado == 5:  # vitoria
            if self.__nivel_atual == 'mercado':
                self.__nivel_atual = 'cozinha'
            elif self.__nivel_atual == 'cozinha':
                self.__nivel_atual = 'restaurante'
        # dificuldade principal(temporario)
        elif self.__estado == 2 or self.__estado == 1:
            self.__nivel_atual = 'mercado'

    def MudaEstados(self):
        if self.__timer_sec <= -1 and self.__estado == 0:  # jogando
            self.__estado = Estados(6)  # derrota

        if self.__fase != None and self.__fase.vitoria == True and self.__estado == 0:
            self.__estado = Estados(5)

        if self.__estado != 0:  # jogando, pausa
            if self.__teclas_clicadas['enter']:
                self.__som_botao.play()
                if self.__estado == 1:  # principal
                    # mudar para dificuldade -------------------------------
                    if self.__menu_prin.opcao == 'Jogar':
                        self.__estado = Estados(2)  # dificuldade
                    elif self.__menu_prin.opcao == 'Tutorial':
                        self.__estado = Estados(3)  # tutorial
                    elif self.__menu_prin.opcao == 'Créditos':
                        self.__estado = Estados(4)  # creditos
                    elif self.__menu_prin.opcao == 'Sair':
                        self.__rodando = False

                elif self.__estado == 2:  # dificuldade
                    self.__dificuldade = self.__menu_dif.opcao
                    self.novaFase()
                    self.__estado = Estados(0)  # jogando

                elif self.__estado == 5:  # vitoria
                    if self.__nivel_atual == 'restaurante':
                        self.__estado = Estados(1)
                    else:
                        self.novaFase()
                        self.__estado = Estados(0)

                elif self.__estado == 6:  # derrota
                    self.novaFase()
                    self.__estado = Estados(0)

                elif self.__estado == 7:  # pausa
                    self.__estado = Estados(0)

            elif self.__teclas_clicadas['backspace']:
                self.__som_botao.play()
                if (  # dificuldade, tutorial, creditos, vitoria, derrota
                    self.__estado == 2 or self.__estado == 3 or self.__estado == 4 or
                    self.__estado == 5 or self.__estado == 6
                ):
                    self.__estado = Estados(1)  # principal

                elif self.__estado == 7:  # pausa
                    self.__estado = Estados(1)

        if self.__estado == 0 or self.__estado == 7:
            if self.__teclas_clicadas['esc']:
                self.__som_botao.play()
                if self.__estado == 0:
                    self.__estado = Estados(7)
                elif self.__estado == 7:
                    self.__estado = Estados(0)

    def reiniciaTimer(self):
        self.__timer_sec = 120
        pygame.time.set_timer(self.__timer, 1000)

from constants import (
    WIDTH, HEIGHT, FONT_SIZE_MESSAGE, PLAYER_SPEED,
    BACKGROUND_SPEED, HAZARD_SPEED, MARGEM_DIREITA,
    MARGEM_ESQUERDA, FRAME_TIME_MS, COLLISION_DELAY,
)
import pygame
import random
import time
from entities.player import Player
from entities.background import Background
from entities.hazard import Hazard
from score import Score

class Game:
    # movimento do Player
    DIREITA = pygame.K_RIGHT
    ESQUERDA = pygame.K_LEFT


    def __init__(self):

        """
        Função que inicializa o pygame, define a resolução da tela,
        caption, e desabilita o mouse.
        """

        self.width = WIDTH
        self.height = HEIGHT
        self.run = True
        self.background = None
        self.player = None
        self.hazards = []
        self.mudar_x = 0.0

        pygame.init()

        self.screen = pygame.display.set_mode((self.width, self.height))  # tamanho da tela
        self.screen_size = self.screen.get_size()

        pygame.mouse.set_visible(0)
        pygame.display.set_caption('Viagem Espacial')

        # fontes
        my_font = pygame.font.Font("Fonts/Fonte4.ttf", FONT_SIZE_MESSAGE)

        # Mensagens para o jogador
        self.render_text_bateulateral = my_font.render("COLISÃO!", 0,(255, 255, 255))  # ("texto", opaco/transparente 0/1, cor do texto)
        self.render_text_perdeu = my_font.render("GAME OVER!", 0, (255, 0, 0))  # ("texto, opaco/transparente 0/1, cor do texto)

    # init()

    def handle_events(self):
        """
        Trata o evento e toma a ação necessária.
        """
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.run = False

            # se clicar em qualquer tecla, entra no if
            if event.type == pygame.KEYDOWN:
                # se clicar na seta da esquerda, anda 3 para a esquerda no eixo x
                if event.key == self.ESQUERDA:
                    self.mudar_x = -PLAYER_SPEED
                # se clicar na seta da direita, anda 3 para a direita no eixo x
                if event.key == self.DIREITA:
                    self.mudar_x = PLAYER_SPEED

            # se soltar qualquer tecla, não faz nada
            if event.type == pygame.KEYUP:
                if event.key == self.ESQUERDA or event.key == self.DIREITA:
                    self.mudar_x = 0

    # handle_events()

    def elements_update(self, dt):
        self.background.update(dt)
    # elements_update()

    def elements_draw(self):
        self.background.draw(self.screen)
    # elements_draw()

    # Desenha o Player
    def draw_player (self, x, y):
        self.player.draw (self.screen, x, y)
    # draw_player()

    # Desenha Hazard
    def draw_hazard (self, hzrd, x, y):
        self.hazards[hzrd].draw(self.screen, x, y)
    # draw_hazard()

    # Define as posições dos objetos para criar o movimento
    def move_background (self, obj_movL_x, obj_movL_y, obj_movR_x, obj_movR_y):
        self.background.move (self.screen, obj_movL_x, obj_movL_y, obj_movR_x,obj_movR_y)
    # move_background()

    def initialize_game(self):
        self.scoreboard = Score()
        self.background = Background()
        self.mudar_x = 0.0

        self.movL_x = 0
        self.movL_y = 0
        self.movR_x = MARGEM_DIREITA
        self.movR_y = 0

        player_x = (self.width - 56) / 2
        player_y = self.height - 125
        self.player = Player(player_x, player_y)

        hazard_x = random.randrange(125, 660)
        hazard_y = -500
        self.hazards = [
            Hazard("Images/nave.png", hazard_x, hazard_y),
            Hazard("Images/satelite.png", hazard_x, hazard_y),
            Hazard("Images/cometa.png", hazard_x, hazard_y),
            Hazard("Images/planeta.png", hazard_x, hazard_y),
            Hazard("Images/ameaca.png", hazard_x, hazard_y),
        ]
        self.hazard_index = 0

    def update_background(self):
        self.move_background(
            self.movL_x,
            self.movL_y,
            self.movR_x,
            self.movR_y,
        )
        self.movL_y += BACKGROUND_SPEED
        self.movR_y += BACKGROUND_SPEED

        if self.movL_y > 640 and self.movR_y > 640:
            self.movL_y -= 640
            self.movR_y -= 640

    def update_player(self):
        self.player.move(self.mudar_x, 0)
        self.draw_player(self.player.x, self.player.y)

    def update_hazard(self):
        hazard = self.hazards[self.hazard_index]
        hazard.move(0, HAZARD_SPEED / 4)
        self.draw_hazard(self.hazard_index, hazard.x, hazard.y)
        hazard.move(0, HAZARD_SPEED)

        if hazard.y > self.height:
            self.hazard_index = random.randrange(len(self.hazards))
            self.hazards[self.hazard_index].reaparecer()
            self.scoreboard.counter_passed_hazard()

    def check_collisions(self):
        if (
            self.player.limite_direito() > MARGEM_DIREITA
            or self.player.limite_esquerdo() < MARGEM_ESQUERDA
        ):
            self.screen.blit(self.render_text_bateulateral, (80, 200))
            pygame.display.update()
            time.sleep(COLLISION_DELAY)
            self.initialize_game()
            return

        hazard = self.hazards[self.hazard_index]
        if self.player.y < hazard.y + hazard.image.get_height():
            if self.player.x > hazard.x or self.player.x > hazard.x - 56:
                if (
                    self.player.x < hazard.x + hazard.image.get_width()
                    or self.player.x < hazard.x - 56
                ):
                    self.screen.blit(self.render_text_perdeu, (80, 200))
                    pygame.display.update()
                    time.sleep(COLLISION_DELAY)
                    self.run = False

    def draw_hud(self):
        self.scoreboard.draw(self.screen)

    def loop(self):
        """
        Laço principal
        """
        self.initialize_game()

        # Inicializamos o relogio e o dt que vai limitar o valor de FPS
        # frames por segundo do jogo
        clock = pygame.time.Clock()
        dt = FRAME_TIME_MS

        # assim iniciamos o loop principal do programa
        while self.run:
            clock.tick(1000 / dt)

            # Handle Input Events
            self.handle_events()

            # Atualiza Elementos
            self.elements_update(dt)

            # Desenha o background buffer
            self.elements_draw()

            self.update_background()
            self.update_player()
            self.draw_hud()
            self.update_hazard()
            self.check_collisions()

            # atualizando a tela
            pygame.display.update()
            clock.tick(2000)

        # while self.run
    # loop()
# Game:

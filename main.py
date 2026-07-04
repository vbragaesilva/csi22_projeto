# Código para refatoração - Viagem Espacial

import pygame
import random
import time

WIDTH = 800
HEIGHT = 600
MARGEM_ESQUERDA = 60
MARGEM_DIREITA = 740

PLAYER_WIDTH = 90
PLAYER_HEIGHT = 90
HAZARD_WIDTH = 130
HAZARD_HEIGHT = 130
PLAYER_SPEED = 3
BACKGROUND_SPEED = 5
HAZARD_SPEED = 7
SCORE_PER_HAZARD = 10
COLLISION_DELAY = 3
FONT_SIZE_MESSAGE = 100
FONT_SIZE_SCORE = 35
FRAME_TIME_MS = 16

class Background:
    """
    Esta classe define o Plano de Fundo do jogo
    """
    image = None
    margin_left = None
    margin_right = None

    def __init__(self):

        background_fig = pygame.image.load("Images/background.png")
        background_fig.convert()
        self.image = background_fig

        margin_left_fig = pygame.image.load("Images/margin_1.png")
        margin_left_fig.convert()
        margin_left_fig = pygame.transform.scale(margin_left_fig, (MARGEM_ESQUERDA, HEIGHT))
        self.margin_left = margin_left_fig

        margin_right_fig = pygame.image.load("Images/margin_2.png")
        margin_right_fig.convert()
        margin_right_fig = pygame.transform.scale(margin_right_fig, (WIDTH-MARGEM_DIREITA, HEIGHT))
        self.margin_right = margin_right_fig
    # __init__()

    def update(self, dt):
        pass
    # update()

    def draw(self, screen):
        screen.blit(self.image, (0, 0))
        screen.blit(self.margin_left, (0, 0))
        screen.blit(self.margin_right, (MARGEM_DIREITA, 0))
    # draw()

    # Define posições do Plano de Fundo para criar o movimento
    def move (self, screen, movL_x, movL_y, movR_x, movR_y):

        #movimento background
        screen.blit(self.image, (movL_x, movL_y))
        screen.blit(self.image, (movL_x, movL_y + 600))
        screen.blit(self.image, (movL_x, movL_y + 1200))
        screen.blit(self.image, (movL_x, movL_y + 1800))
        screen.blit(self.image, (movL_x, movL_y + 2400))
        screen.blit(self.image, (movL_x, movL_y + 3000))
        screen.blit(self.image, (movL_x, movL_y - 600))
        screen.blit(self.image, (movL_x, movL_y - 1200))
        screen.blit(self.image, (movL_x, movL_y - 1800))
        screen.blit(self.image, (movL_x, movL_y - 2400))
        screen.blit(self.image, (movL_x, movL_y - 3000))
        screen.blit(self.image, (movL_x, movL_y - 3600))
        screen.blit(self.image, (movL_x, movL_y - 4200))
        screen.blit(self.image, (movL_x, movL_y - 4800))

        # movimento margem esquerda
        screen.blit(self.margin_left, (movL_x, movL_y))
        screen.blit(self.margin_left, (movL_x, movL_y + 600))
        screen.blit(self.margin_left, (movL_x, movL_y + 1200))
        screen.blit(self.margin_left, (movL_x, movL_y + 1800))
        screen.blit(self.margin_left, (movL_x, movL_y + 2400))
        screen.blit(self.margin_left, (movL_x, movL_y + 3000))
        screen.blit(self.margin_left, (movL_x, movL_y - 600))
        screen.blit(self.margin_left, (movL_x, movL_y - 1200))
        screen.blit(self.margin_left, (movL_x, movL_y - 1800))
        screen.blit(self.margin_left, (movL_x, movL_y - 2400))
        screen.blit(self.margin_left, (movL_x, movL_y - 3000))
        screen.blit(self.margin_left, (movL_x, movL_y - 3600))
        screen.blit(self.margin_left, (movL_x, movL_y - 4200))
        screen.blit(self.margin_left, (movL_x, movL_y - 4800))

        # movimento margem direita
        screen.blit(self.margin_right, (movR_x, movR_y))
        screen.blit(self.margin_right, (movR_x, movR_y + 600))
        screen.blit(self.margin_right, (movR_x, movR_y + 1200))
        screen.blit(self.margin_right, (movR_x, movR_y + 1800))
        screen.blit(self.margin_right, (movR_x, movR_y + 2400))
        screen.blit(self.margin_right, (movR_x, movR_y + 3000))
        screen.blit(self.margin_right, (movR_x, movR_y - 600))
        screen.blit(self.margin_right, (movR_x, movR_y - 1200))
        screen.blit(self.margin_right, (movR_x, movR_y - 1800))
        screen.blit(self.margin_right, (movR_x, movR_y - 2400))
        screen.blit(self.margin_right, (movR_x, movR_y - 3000))
        screen.blit(self.margin_right, (movR_x, movR_y - 3600))
        screen.blit(self.margin_right, (movR_x, movR_y - 4200))
        screen.blit(self.margin_right, (movR_x, movR_y - 4800))
    # move()
# Background:

class Player:
    """
    Classe Jogador
    """
    image = None
    x = None
    y = None

    def __init__(self, x, y):
        player_fig = pygame.image.load("Images/player.png")
        player_fig.convert()
        player_fig = pygame.transform.scale(player_fig, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image = player_fig
        self.x = x
        self.y = y
    # __init__()

    # Desenhar Player
    def draw (self, screen, x, y):
        screen.blit(self.image, (x, y))
    #draw()
# Player:

class Hazard:

    image = None
    x = None
    y = None

    def __init__(self, img, x, y):
        hazard_fig = pygame.image.load(img)
        hazard_fig.convert()
        hazard_fig = pygame.transform.scale(hazard_fig, (HAZARD_WIDTH, HAZARD_HEIGHT))
        self.image = hazard_fig
        self.x = x
        self.y = y
    # __init__()

    # Desenhar Hazard
    def draw (self, screen, x, y):
        screen.blit(self.image, (x, y))
    #draw()
# Hazard:

class Game:
    screen = None
    screen_size = None
    width = WIDTH
    height = HEIGHT
    run = True
    background = None
    player = None
    hazard_1 = hazard_2 = hazard_3 = hazard_4 = hazard_5 = None
    render_text_bateulateral = None
    render_text_perdeu = None

    # movimento do Player
    DIREITA = pygame.K_RIGHT
    ESQUERDA = pygame.K_LEFT
    mudar_x = 0.0


    def __init__(self, size, fullscreen):

        """
        Função que inicializa o pygame, define a resolução da tela,
        caption, e desabilita o mouse.
        """

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
        if hzrd == 0:
            self.hazard_1.draw(self.screen, x, y)
        elif hzrd == 1:
            self.hazard_2.draw(self.screen, x, y)
        elif hzrd == 2:
            self.hazard_3.draw(self.screen, x, y)
        elif hzrd == 3:
            self.hazard_4.draw(self.screen, x, y)
        elif hzrd == 4:
            self.hazard_5.draw(self.screen, x, y)
    # draw_hazard()

    # Define as posições dos objetos para criar o movimento
    def move_background (self, obj_movL_x, obj_movL_y, obj_movR_x, obj_movR_y):
        self.background.move (self.screen, obj_movL_x, obj_movL_y, obj_movR_x,obj_movR_y)
    # move_background()

    # Informa a quantidade de hazard que passaram e a Pontuação
    def score_card(self, screen, h_passou, score):
        font = pygame.font.SysFont(None, FONT_SIZE_SCORE)
        passou = font.render("Passou: " + str(h_passou), True, (255, 255, 128))
        score = font.render("Score: " + str(score), True, (253, 231, 32))
        screen.blit(passou, (0, 50))
        screen.blit(score, (0, 100))
    #score_card()

    def loop(self):
        """
        Laço principal
        """
        score = 0
        h_passou = 0

        # variáveis para movimento de Plano de Fundo/Background
        velocidade_background = BACKGROUND_SPEED
        velocidade_hazard = HAZARD_SPEED

        faixaA_x = 375
        faixaA_y = 0
        hzrd = 0
        h_x = random.randrange(125, 660)
        h_y = -500

        # Info Hazard
        h_width = HAZARD_WIDTH #55
        h_height = HAZARD_HEIGHT #120

        # movimento da margem esquerda
        movL_x = 0
        movL_y = 0

        # movimento da margem direita
        movR_x = MARGEM_DIREITA
        movR_y = 0

        # Criar o Plano de fundo
        self.background = Background()

        # Posicao do Player
        x = (self.width - 56) / 2
        y = self.height - 125

        # Criar o Player
        self.player = Player(x, y)

        # Criar Harzard_1
        self.hazard_1 = Hazard("Images/nave.png", h_x, h_y)

        # Criar Harzard_2
        self.hazard_2 = Hazard("Images/satelite.png", h_x, h_y)

        # Criar Harzard_3
        self.hazard_3 = Hazard("Images/cometa.png", h_x, h_y)

        # Criar Harzard_4
        self.hazard_4 = Hazard("Images/planeta.png", h_x, h_y)

        # Criar Harzard_5
        self.hazard_5 = Hazard("Images/ameaca.png", h_x, h_y)

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

            # adiciona movimento ao background

            self.move_background (movL_x, movL_y, movR_x, movR_y)
            movL_y = movL_y + velocidade_background
            movR_y = movR_y + velocidade_background

            #se a imagem ultrapassar a extremidade da tela, move de volta
            if movL_y > 640 and movR_y > 640:
                movL_y -= 640
                movR_y -= 640

            # Altera a coordenada x do Player de acordo comas mudanças no event_handle() para ele se mover
            x = x + self.mudar_x

            # Mostrar Player
            self.draw_player (x, y)

            # Mostrar score
            self.score_card(self.screen, h_passou, score)

            # Restrições do movimento do Player
            # Se o Player bate na lateral não é Game Over
            # CONSERTAR: ADICIONAR METODOS PARA LIMITES ESQUERDOS E DIREITOS.
            if x > MARGEM_DIREITA - self.player.image.get_width() or x < MARGEM_ESQUERDA + self.player.image.get_width():
                self.screen.blit(self.render_text_bateulateral, (80, 200))
                pygame.display.update()  # atualizar a tela
                time.sleep(COLLISION_DELAY)
                self.loop()
                self.run = False

            # adicionando movimento ao hazard
            h_y = h_y + velocidade_hazard / 4
            self.draw_hazard(hzrd, h_x, h_y)
            h_y = h_y + velocidade_hazard

            # definindo onde hazard vai aparecer, recomeçando a posição do obstaculo e da faixa
            if h_y > self.height:
                h_y = 0 - h_height
                faixaA_y = 0
                h_x = random.randrange(125, 650 - h_height)
                hzrd = random.randint(0, 4)
                # determinando quantos hazard passaram e a pontuação
                h_passou = h_passou + 1
                score = h_passou * SCORE_PER_HAZARD

            # restrições para o game over
            if y < h_y + h_height:
                if x > h_x or x > h_x - 56:
                    if x < h_x + h_width or x < h_x - 56:
                        self.screen.blit(self.render_text_perdeu, (80, 200))
                        pygame.display.update()
                        time.sleep(COLLISION_DELAY)
                        self.run = False

            # atualizando a tela
            pygame.display.update()
            clock.tick(2000)

        # while self.run
    # loop()
# Game:

def main():
    # Cria o objeto game e chama o loop básico
    game = Game("resolution", "fullscreen")
    game.loop()
# main()

# Chama a função main
if __name__ == '__main__':
    main()
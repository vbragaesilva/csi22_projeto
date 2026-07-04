from constants import MARGEM_ESQUERDA, MARGEM_DIREITA, WIDTH, HEIGHT
import pygame
class Background:
    """
    Esta classe define o Plano de Fundo do jogo
    """
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

        ALTURA_TILE = 600
        N_TILES_ACIMA = 8
        N_TILES_ABAIXO = 5

        for i in range(-N_TILES_ACIMA, N_TILES_ABAIXO + 1):
            dy = i * ALTURA_TILE
            screen.blit(self.image,        (movL_x, movL_y + dy))
            screen.blit(self.margin_left,  (movL_x, movL_y + dy))
            screen.blit(self.margin_right, (movR_x, movR_y + dy))
    # move()
# Background:

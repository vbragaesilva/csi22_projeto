from constants import SCORE_PER_HAZARD, FONT_SIZE_SCORE
import pygame

class Score:
    """
    Classe de Pontuacao
    """
    def __init__(self):
        self.hazards_passed = 0
        self.score = 0

    def counter_passed_hazard(self):
        """
        Chamado quando um hazard sai da tela sem colidir
        """
        self.hazards_passed = self.hazards_passed + 1
        self.score = self.hazards_passed * SCORE_PER_HAZARD

    def draw(self, screen):
        """
        Informa a quantidade de hazard que passaram e a Pontuação
        """
        font = pygame.font.SysFont(None, FONT_SIZE_SCORE)
        passou_text = font.render(f"Passou: {self.hazards_passed}", True, (255, 255, 128))
        score_text = font.render(f"Score: {self.score}", True, (253, 231, 32))
        screen.blit(passou_text, (0, 50))
        screen.blit(score_text, (0, 100))

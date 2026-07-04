from constants import PLAYER_WIDTH, PLAYER_HEIGHT
from object import Object


class Player(Object):
    """
    Classe Jogador
    """
    def __init__(self, x, y):
        super().__init__(
            "Images/player.png",
            x,
            y,
            (PLAYER_WIDTH, PLAYER_HEIGHT),
            margem_esquerda=20,
            margem_direita=20,
        )
    # __init__()
# Player:

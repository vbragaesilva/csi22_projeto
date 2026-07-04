import random

from constants import (
    HAZARD_WIDTH,
    HAZARD_HEIGHT,
    MARGEM_ESQUERDA,
    MARGEM_DIREITA,
)
from .object import Object


class Hazard(Object):

    def __init__(self, img, x, y):
        super().__init__(img, x, y, (HAZARD_WIDTH, HAZARD_HEIGHT))
    # __init__()

    def reaparecer(self):
        self.x = random.randrange(
            MARGEM_ESQUERDA,
            MARGEM_DIREITA - self.image.get_width() + 1,
        )
        self.y = -self.image.get_height()

        return self.x, self.y
# Hazard:

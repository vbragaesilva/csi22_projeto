from constants import HAZARD_WIDTH, HAZARD_HEIGHT
from .object import Object


class Hazard(Object):

    def __init__(self, img, x, y):
        super().__init__(img, x, y, (HAZARD_WIDTH, HAZARD_HEIGHT))
    # __init__()
# Hazard:

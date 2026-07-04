from abc import ABC, abstractmethod

import pygame


class Object(ABC):
    @abstractmethod
    def __init__(self, img, x, y, size, margem_esquerda=0, margem_direita=0):
        object_fig = pygame.image.load(img)
        object_fig.convert()
        self.image = pygame.transform.scale(object_fig, size)
        self.x = x
        self.y = y
        self.margem_esquerda = margem_esquerda
        self.margem_direita = margem_direita

    def draw(self, screen, x, y):
        screen.blit(self.image, (x, y))

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

    def limite_esquerdo(self):
        return self.x + self.margem_esquerda

    def limite_direito(self):
        return self.x + self.image.get_width() - self.margem_direita

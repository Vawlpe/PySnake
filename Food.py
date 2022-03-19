import random
import pygame
import GLOBALS as G


class Food(object):
    def __init__(self):
        self.pos = (random.randint(0, G.GRID_W - 1) * G.GRID_S, random.randint(0, G.GRID_H - 1) * G.GRID_S)
        self.size = 1
        self.color = (255, 255, 255)

    def update(self):
        pass

    def draw(self, surface):
        pygame.draw.rect(
            surface,
            self.color,
            pygame.Rect(self.pos, (G.GRID_S * self.size, G.GRID_S * self.size)),
            0,
            10 * self.size
        )

    def consume(self, consumer):
        self.__class__.__init__(self)

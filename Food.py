import random
import pygame
import GLOBALS as G


class Food(object):
    def __init__(self):
        self.pos = (random.randint(0, G.GRID_W-1) * G.GRID_S, random.randint(0, G.GRID_H-1) * G.GRID_S)
        self.size = 2 if random.randint(0, 100) > 75 else 1
        self.color = G.COLORS["SmallFruit"] if self.size == 1 else G.COLORS["BigFruit"]
        self.timer = 100

    def update(self):
        if self.size == 1:
            return

        if self.timer > 0:
            self.timer -= 1
        else:
            G.GAME.objects["food"] = Food()

    def draw(self, surface):
        pygame.draw.rect(
            surface,
            self.color,
            pygame.Rect(self.pos, (G.GRID_S * self.size, G.GRID_S * self.size)),
            0,
            10 * self.size
        )
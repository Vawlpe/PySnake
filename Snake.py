import numpy
import pygame

import Food
import GLOBALS as G
import Game


class Snake(object):
    def __init__(self):
        self.length = 2
        self.positions = [((G.SCREEN_W / 2), (G.SCREEN_H / 2))]
        self.dir = G.DIRECTIONS[pygame.K_UP]

    def get_head(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.dir:
            return

        self.dir = point

    def move(self):
        cur = self.get_head()
        x, y = self.dir
        new = (((cur[0] + (x * G.GRID_S)) % G.SCREEN_W), ((cur[1] + (y * G.GRID_S)) % G.SCREEN_H))
        if new in self.positions:
            G.GAME = Game.Game()
        self.positions.insert(0, new)
        if len(self.positions) > self.length:
            self.positions.pop()

    def eat(self):
        if self.get_head() == G.GAME.objects["food"].pos:
            self.length += 1
            G.GAME.score += 10 if G.GAME.objects["food"].size == 1 else 100
            G.GAME.objects["food"] = Food.Food()

    def update(self):
        self.move()
        self.eat()

    def draw(self, surface):
        for i, p in enumerate(self.positions):
            pygame.draw.rect(
                surface,
                tuple(numpy.subtract(G.COLORS["Snake"], (0, min((i * 100) / self.length, 255), 0))),
                pygame.Rect((p[0], p[1]), (G.GRID_S, G.GRID_S)),
                0,
                5
            )

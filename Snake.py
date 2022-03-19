import numpy
import pygame

import GLOBALS as G
import Game
from Food import Food


class Snake(object):
    def __init__(self):
        self.length = 2
        self.positions = [((G.SCREEN_W / 2), (G.SCREEN_H / 2))]
        self.dir = G.DIRECTIONS[pygame.K_UP]
        self.score = 0
        self.speed = 10
        self.reset_speed = 10
        self.reset_speed_timer = 0

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

        # Reset game
        if new in self.positions:
            G.GAME = Game.Game()

        # Move tail
        self.positions.insert(0, new)
        if len(self.positions) > self.length:
            self.positions.pop()

    def eat(self):
        # Filter game-objects
        col = {
            key: value for (key, value)
            in G.GAME.objects.items()
            if isinstance(value, Food)              # Must be food
            and value.pos == self.get_head()        # Must overlap head
        }
        for c in col.values():
            c.consume(consumer=self)                # Call consume method of every food collision found

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

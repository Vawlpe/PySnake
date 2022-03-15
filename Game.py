import pygame

import Food
import GLOBALS as G
import sys

import Snake


class Game(object):
    def __init__(self):
        self.objects = {
            "snake": Snake.Snake(),
            "food": Food.Food()
        }
        self.score = 0

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in G.DIRECTIONS:
                    self.objects["snake"].turn(G.DIRECTIONS[event.key])

        for k, v in self.objects.items():
            v.update()

    def draw(self, surface):
        self.draw_grid(surface)
        for k, v in self.objects.items():
            v.draw(surface)

    def draw_grid(self, surface):
        for y in range(0, int(G.GRID_H)):
            for x in range(0, int(G.GRID_W)):
                pygame.draw.rect(
                    surface,
                    G.COLORS["GridLight"] if (x + y) % 2 == 0 else G.COLORS["GridDark"],
                    pygame.Rect((x * G.GRID_S, y * G.GRID_S), (G.GRID_S, G.GRID_S))
                )

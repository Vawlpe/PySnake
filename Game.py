import pygame
import GLOBALS as G
import sys

from AppleFood import Apple
from LemonFood import Lemon
from OrangeFood import Orange
from Snake import Snake


class Game(object):
    def __init__(self):
        self.objects = {}
        self.objects["snake"]  = Snake()
        self.objects["apple"]  = Apple()
        self.objects["orange"] = Orange()
        self.objects["lemon"]  = Lemon()

    def update(self):
        turnedThisFrame = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_q, pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_r:
                    self.__class__.__init__(self)
                elif event.key in G.DIRECTIONS and not turnedThisFrame:
                    turnedThisFrame = True
                    self.objects["snake"].turn(G.DIRECTIONS[event.key])

        for k, v in self.objects.items():
            v.update()

    def draw(self, surface):
        self.draw_grid(surface)
        for k, v in self.objects.items():
            v.draw(surface)

    @staticmethod
    def draw_grid(surface):
        for y in range(0, int(G.GRID_H)):
            for x in range(0, int(G.GRID_W)):
                pygame.draw.rect(
                    surface,
                    G.COLORS["GridLight"] if (x + y) % 2 == 0 else G.COLORS["GridDark"],
                    pygame.Rect((x * G.GRID_S, y * G.GRID_S), (G.GRID_S, G.GRID_S))
                )

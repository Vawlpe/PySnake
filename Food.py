import random
import pygame
import GLOBALS as G


class Food(object):
    def __init__(self):
        self.pos = (random.randint(0, G.GRID_W - 1) * G.GRID_S, random.randint(0, G.GRID_H - 1) * G.GRID_S)
        self.size = 1
        self.color = (255, 255, 255)

    def update(self):
        # Make sure Food objects don't spawn in illegal positions
        while self.pos in [
            *G.GAME.objects["snake"].positions,        # Snake positions
            (dir+G.GAME.objects["snake"].positions[0]  # Safe-space around snake head
                for dir in [tuple([n * x for n in d])
                    for d in G.DIRECTIONS.values()
                        for x in range(1,6)]),
            (o.pos for o in G.GAME.objects.values() if not isinstance(o, Snake)) # Other object positions
        ]:
            self.pos = (random.randint(0, G.GRID_W - 1) * G.GRID_S, random.randint(0, G.GRID_H - 1) * G.GRID_S)

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

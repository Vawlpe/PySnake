import pygame
import Game

# Global variables
SCREEN_W = 480
SCREEN_H = 480

GRID_S = 20
GRID_W = SCREEN_W / GRID_S
GRID_H = SCREEN_H / GRID_S

DIRECTIONS = {
    pygame.K_UP: (0, -1),
    pygame.K_DOWN: (0, 1),
    pygame.K_LEFT: (-1, 0),
    pygame.K_RIGHT: (1, 0),
}

COLORS = {
    "GridLight": (175, 140, 215),
    "GridDark": (115, 55, 175),
    "Snake": (0, 255, 0),
    "Apple": (255, 0, 0),
    "Orange": (255, 120, 0),
    "Lemon": (255, 255, 0)
}

GAME = Game.Game()

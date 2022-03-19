import pygame
import GLOBALS as G


def main():
    pygame.init()

    screen = pygame.display.set_mode((G.SCREEN_H, G.SCREEN_W), 0, 32)
    clock = pygame.time.Clock()

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    while 1:
        if G.GAME.objects["snake"].reset_speed_timer > 0:
            G.GAME.objects["snake"].reset_speed_timer -= 1
        else:
            G.GAME.objects["snake"].speed = G.GAME.objects["snake"].reset_speed
        clock.tick(G.GAME.objects["snake"].speed)
        G.GAME.update()
        G.GAME.draw(surface)
        screen.blit(surface, (0, 0))
        screen.blit(
            pygame.font.SysFont("helvetica", 24, True)
            .render("Score: {0}".format(G.GAME.objects["snake"].score), True, (0, 0, 0)),
            (5, 10)
        )
        pygame.display.update()


if __name__ == "__main__":
    main()

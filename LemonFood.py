import random
import GLOBALS as G
from Food import Food


class Lemon(Food):
    def __init__(self):
        super().__init__()
        self.color = G.COLORS["Lemon"]
        self.NextTimer = random.randint(100, 500)
        self.StayTimer = 100

    def update(self):
        if self.NextTimer > 0:
            self.NextTimer -= 1
        elif self.StayTimer > 0:
            self.StayTimer -= 1
        else:
            self.__init__()

        super().update()

    def draw(self, surface):
        if self.NextTimer > 0:
            return
        super().draw(surface)

    def consume(self, consumer):
        consumer.score = consumer.score + 50
        consumer.length = consumer.length + 1
        consumer.speed = 20
        consumer.reset_speed_timer = 100
        super().consume(consumer)

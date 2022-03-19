import random
import GLOBALS as G
from Food import Food


class Orange(Food):
    def __init__(self):
        super().__init__()
        self.color = G.COLORS["Orange"]
        self.NextTimer = random.randint(100, 200)
        self.StayTimer = 100

    def update(self):
        print("Orange : {0}, {1}".format(self.NextTimer, self.StayTimer))
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
        consumer.score += 100
        consumer.length += 1
        super().consume(consumer)

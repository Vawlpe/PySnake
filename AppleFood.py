import GLOBALS as G
from Food import Food


class Apple(Food):
    def __init__(self):
        super().__init__()
        self.color = G.COLORS["Apple"]

    def update(self):
        super().update()

    def draw(self, surface):
        super().draw(surface)

    def consume(self, consumer):
        consumer.score = consumer.score + 10
        consumer.length = consumer.length + 1
        super().consume(consumer)

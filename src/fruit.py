import random
from pygame.sprite import Sprite
from pygame.image import load
from pygame.transform import scale

from .utils import Point, get_edges
from .map import Map


class Fruit(Sprite):
    def __init__(self, map: Map):
        super().__init__()

        self.map = map
        self.image = scale(load("images/snake.png"), (10, 10))

        self.rect = self.image.get_rect(center=self.random_position())

    def update(self, change_position=False):
        if self.has_collisions() or change_position:
            self.rect.x, self.rect.y = self.random_position()

    def has_collisions(self):
        return len(list(filter(self.map.is_infected, get_edges(self)))) > 0

    def random_position(self):
        padding = 50
        return Point(
            x=random.randint(padding, self.map.surface.get_width() - padding),
            y=random.randint(padding, self.map.surface.get_height() - padding),
        )

from pygame.sprite import Sprite
from collections import namedtuple
from typing import NamedTuple

Size = namedtuple("Size", "width heigth")


class Point(NamedTuple):
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


def get_edges(sprite: Sprite):
    x, y = sprite.rect.x, sprite.rect.y
    sizeX, sizeY = sprite.rect.size
    return [
        Point(x, y),
        Point(x, y + sizeY),
        Point(x + sizeX, y),
        Point(x + sizeX, y + sizeY),
    ]

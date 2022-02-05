from functools import partial
from pygame import Color
from pygame.surface import Surface
from abc import ABC
from typing import Callable, Optional
from random import randint
from dataclasses import dataclass

from .map import Map
from .utils import Point
from .game import GameObject
from .floodfill import dsf_flood_fill, bsf_flood_fill


class Infecter(ABC, GameObject):
    def __init__(
        self, infect: Callable, start: Point, step: int, color: Optional[Color] = None
    ):
        if not color:
            color = random_color()

        self.infect_template = partial(infect, point=start, colorFill=color)
        self.infect_generator = None
        self.step = step

    def infect_map(self, map: Map):
        self.infect_generator = self.infect_template(surface=map.game_surface)
        map.add_object(self)

    def update(self):
        if not self.infect_generator:
            return

        for _ in range(self.step):
            next(self.infect_generator)

    def draw(self, surface: Surface):
        ...


class InfecterBFS(Infecter):
    def __init__(self, start: Point, color: Optional[Color] = None, step: int = 20):
        super().__init__(bsf_flood_fill, start, step, color)


class InfecterDFS(Infecter):
    def __init__(self, start: Point, color: Optional[Color] = None, step: int = 20):
        super().__init__(dsf_flood_fill, start, step, color)


def random_color():
    random_color_generator = partial(randint, 0, 255)
    return Color(
        random_color_generator(), random_color_generator(), random_color_generator()
    )


@dataclass
class InfecterBuilder:
    infecter: Infecter
    start: Point
    step: int

    def build(self) -> Infecter:
        return self.infecter(start=self.start, step=self.step)
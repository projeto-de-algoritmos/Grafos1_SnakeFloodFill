from pygame import Color
from pygame.surface import Surface
from typing import Iterable
from queue import Queue, LifoQueue

from .game import RemoveGameObject
from .utils import Point, Size


def bsf_flood_fill(point: Point, surface: Surface, colorFill: Color):
    color = surface.get_at(point)
    surface_size = Size(surface.get_width(), surface.get_height())

    if color == colorFill:
        return

    q = Queue()
    q.put(point)
    surface.set_at(point, colorFill)
    while not q.empty():
        point = q.get()
        for point_adj in get_adj_points(point, surface_size):
            if surface.get_at(point_adj) == color:
                surface.set_at(point_adj, colorFill)
                q.put(point_adj)
                yield
    raise RemoveGameObject


def dsf_flood_fill(point: Point, surface: Surface, colorFill: Color):
    color = surface.get_at(point)
    surface_size = Size(surface.get_width(), surface.get_height())

    if color == colorFill:
        return

    q = LifoQueue()
    q.put(point)
    surface.set_at(point, colorFill)
    while not q.empty():
        point = q.get()
        for point_adj in get_adj_points(point, surface_size):
            if surface.get_at(point_adj) == color:
                surface.set_at(point_adj, colorFill)
                q.put(point_adj)
                yield
    raise RemoveGameObject


ADJ_POINTS = [Point(-1, 0), Point(1, 0), Point(0, -1), Point(0, 1)]


def get_adj_points(point: Point, surface_size: Size) -> Iterable[Point]:
    points = map(lambda adj: adj + point, ADJ_POINTS)
    is_point_valid = lambda p: is_within_bounds(p, surface_size)
    return filter(is_point_valid, points)


def is_within_bounds(point: Point, surface_size: Size) -> bool:
    return 0 <= point.x < surface_size.width and 0 <= point.y < surface_size.heigth

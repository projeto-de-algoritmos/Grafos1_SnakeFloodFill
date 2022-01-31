from pygame import Color
from pygame.surface import Surface
from typing import Iterable
from queue import Queue
from point import Point


def dsf_flood_fiil(point: Point, superface: Surface, colorFill: Color):
    color = superface.get_at(point.get())
    display_size = (superface.get_width(), superface.get_height())
    if color == colorFill:
        return

    q = Queue()
    q.put(point)
    superface.set_at(point.get(), colorFill)
    while not q.empty():
        point = q.get()
        for point_adj in get_adj_points(point, display_size):
            if superface.get_at(point_adj.get()) == color:
                superface.set_at(point_adj.get(), colorFill)
                q.put(point_adj)
                yield

def get_adj_points(point: Point, display_size) -> Iterable[Point]:
    adj_points = [Point(-1, 0), Point(1, 0), Point(0, -1), Point(0, 1)]
    points = map(lambda adj: adj + point, adj_points)
    is_point_valid = lambda p: is_in_bounds(p, display_size)
    return filter(is_point_valid, points)

def is_in_bounds(point: Point, display_size) -> bool:
    return (
        point.x >= 0
        and point.x < display_size[0]
        and point.y >= 0
        and point.y < display_size[1]
    )

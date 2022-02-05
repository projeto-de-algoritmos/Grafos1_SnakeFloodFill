from dataclasses import dataclass
from .utils import Point, Size


@dataclass
class GameConfig:

    fps: int
    title: str

    window_size: Size
    map_size: Size
    map_start: Point

    score_start: Point
    game_over_start: Point
    final_score_start: Point

    music: str

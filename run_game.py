from pygame import Color
from src.infecter import InfecterBFS, InfecterDFS
from src.utils import Point, Size
from src.snake_game import SnakeGame
from src.config import GameConfig

config = GameConfig(
    title="Snake Flood Fill",
    fps=15,
    window_size=Size(800, 600),
    map_size=Size(600, 430),
    map_start=Point(101, 71),
    game_over_start=Point(200, 200),
    final_score_start=Point(330, 270),
    score_start=Point(340, 550),
)

game = SnakeGame(config)

game.add_infecter(InfecterBFS(start=Point(0, 0)))
game.add_infecter(
    InfecterDFS(start=Point(config.map_size[0] - 10, config.map_size[1] - 10))
)

game.run()

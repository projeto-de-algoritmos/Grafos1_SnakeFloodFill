import random
from pygame import Color
from src.infecter import InfecterBFS, InfecterDFS, InfecterBuilder
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
    music="sounds/music.mp3",
)

INFECTERS_POSSIBLE = [
    [
        InfecterBuilder(InfecterBFS, Point(0, 0), 20),
        InfecterBuilder(
            InfecterDFS,
            Point(config.map_size.width - 10, config.map_size.heigth - 10),
            20,
        ),
    ],
    [
        InfecterBuilder(
            InfecterBFS,
            Point(config.map_size.width // 2, config.map_size.heigth // 2),
            10,
        )
    ],
]


game = SnakeGame(config)

for infecter in random.choice(INFECTERS_POSSIBLE):
    game.add_infecter(infecter.build())

game.run()

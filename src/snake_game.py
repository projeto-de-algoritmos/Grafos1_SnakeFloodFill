import pygame
from pygame import font, display
from pygame.sprite import GroupSingle, groupcollide

from .game import Game
from .config import GameConfig
from .map import Map
from .infecter import Infecter
from .board import Board
from .snake import Snake
from .fruit import Fruit

class SnakeGame(Game):
    def __init__(self, config: GameConfig):
        super().__init__(config)

        play_music(config.music)

        self.board = Board(self)
        self.add_object(self.board)

        self.map = Map(self)
        self.add_object(self.map)

        self.fruit = GroupSingle(Fruit(self.map))
        self.snake = Snake(self)

        self.map.add_object(self.fruit)
        self.map.add_object(self.snake)

        self.score_font = font.SysFont("roboto", 40)
        self.points = 0

    def add_infecter(self, infecter: Infecter):
        infecter.infect_map(self.map)

    def update(self):
        super().update()

        if groupcollide(self.snake, self.fruit, False, False):
            self.points += 1
            self.fruit.update(change_position=True)
            self.snake.grow_body()

    def draw(self):
        super().draw()
        score = self.score_font.render(f"Points: {self.points}", True, (0, 0, 0))
        self.surface.blit(score, self.config.score_start)

    def end_game(self):
        game_over_font = font.SysFont("roboto", 100)

        game_over = game_over_font.render("Game Over!", True, (255, 255, 255))

        final_score = self.score_font.render(
            f"Final Score: {self.points}", True, (255, 255, 255)
        )
        self.surface.blit(game_over, self.config.game_over_start)
        self.surface.blit(final_score, self.config.final_score_start)

        display.update()
        
        pygame.mixer.music.stop()

        while self.running:
            self.manage_events()
            pygame.time.delay(100)


def play_music(music: str):
    pygame.mixer.music.load(music)
    pygame.mixer.music.set_volume(.2)
    pygame.mixer.music.play(-1)
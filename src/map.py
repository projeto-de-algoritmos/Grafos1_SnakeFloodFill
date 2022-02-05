import pygame
from pygame import Color
from pygame.surface import Surface

from .utils import Point
from .game import Game, GameSurface

GAME_DEFAULT_COLOR = Color(0, 0, 0, 0)


class Map(GameSurface):
    def __init__(self, game: Game):
        super().__init__(Surface(game.config.map_size, pygame.SRCALPHA, 32))
        self.game_surface = self.surface.copy()
        self.mapStart = game.config.map_start
        self.size = game.config.map_size
        self.game = game

    def draw(self, surface: Surface):
        self.surface.fill(GAME_DEFAULT_COLOR)
        super().draw(self.surface)
        self.surface.blit(self.game_surface, (0, 0))
        self.game.surface.blit(self.surface, self.mapStart)

    def is_infected(self, point: Point):
        return self.game_surface.get_at(point) != GAME_DEFAULT_COLOR

    def is_within_map(self, point: Point):
        return (
            0 < point.x < self.surface.get_width() - 1
            and 0 < point.y < self.surface.get_height() - 1
        )

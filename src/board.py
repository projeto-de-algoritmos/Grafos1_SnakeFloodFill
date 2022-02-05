from pygame import Surface
from .game import GameObject, Game
from pygame.image import load
from pygame.transform import scale


class Board(GameObject):
    def __init__(self, game: Game):
        self.background = scale(load("images/background.png"), game.size)

    def update(self):
        ...

    def draw(self, surface: Surface):
        surface.blit(self.background, (0, 0))

from .board import Board
from .game import Game
from pygame.image import load
from pygame.transform import scale


class SnakeGame(Game):
    def __init__(self, title: str, width: int, height: int, fps: int):
        super().__init__(title, width, height, fps)

        self.initialize()
    
    def initialize(self):
        self.board = Board(self)

        self.add_object(self.board)
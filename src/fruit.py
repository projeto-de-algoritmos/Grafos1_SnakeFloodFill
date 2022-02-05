import pygame
from pygame.sprite import Sprite
from pygame.image import load
from pygame.transform import scale
import random

class Fruit(Sprite):
    def __init__(self, is_infected, surface: pygame.Surface, pos_game: pygame.Surface):
        super().__init__()

        self.image = scale(
            load('../images/snake.png'),
            (5, 5)
        )

        self.is_infected = is_infected
        self.surface = surface
        self.pos_game = pos_game

        self.rect = self.image.get_rect(
            center = self.random_position()
        )

    
    def random_position(self):
        pos_x = random.randint(self.pos_game[0] + 50, self.surface.get_height()-self.pos_game[0] - 50)
        pos_y = random.randint(self.pos_game[1] + 50, self.surface.get_width()-self.pos_game[1] - 50)

        return (pos_x, pos_y)
    
    def update(self):
        if self.is_infected(self):
            self.rect.x, self.rect.y = self.random_position()
import pygame
from pygame.sprite import Sprite
from pygame.image import load
from pygame.transform import scale

from .utils import get_edges


class Snake(Sprite):
    def __init__(self, game):
        super().__init__()

        self.game = game
        self.map = game.map
        self.image = scale(load("images/snake.png"), (20, 20))
        self.rect = self.image.get_rect(
            center=(game.map.surface.get_width() / 2, game.map.surface.get_height() / 2)
        )
        self.velocity = (1, 0)

    def update(self):
        self.read_keys()
        self.manage_collisions()

        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def manage_collisions(self):
        if self.has_collision():
            self.game.end_game()

    def has_collision(self):
        return len(list(filter(self.check_collision, get_edges(self)))) > 0

    def check_collision(self, point):
        return not self.map.is_within_map(point) or self.map.is_infected(point)

    def read_keys(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.velocity = (-1, 0)
        if keys[pygame.K_RIGHT]:
            self.velocity = (1, 0)
        if keys[pygame.K_UP]:
            self.velocity = (0, -1)
        if keys[pygame.K_DOWN]:
            self.velocity = (0, 1)

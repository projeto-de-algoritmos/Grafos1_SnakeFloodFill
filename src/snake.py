import pygame
from pygame.sprite import Sprite, groupcollide
from pygame.image import load
from pygame.transform import scale

class Snake(Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = scale(
            load('../images/snake.png'),
            (20, 20)
        )
        self.rect = self.image.get_rect(
            center=(x, y)
        )
        self.velocity = (1, 0)

    def update(self):
        self.read_keys()

        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

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
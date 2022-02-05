import pygame
from pygame.sprite import Sprite, Group
from pygame.image import load
from pygame.transform import scale


class Body(Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = scale(
            load('../images/snake.png'),
            (10, 10)
        )
        self.rect = self.image.get_rect(
            center=(x, y)
        )
        
    def update(self, x, y):
        self.rect.x = x
        self.rect.y = y

class Snake(Group):
    def __init__(self, x, y):
        super().__init__()

        self.x = x
        self.y = y
        self.add(Body(x, y))
        self.velocity = (10, 0)

    def update(self):
        self.read_keys()
        
        x = self.x
        y = self.y
        
        for b in self.sprites():
            x_before = b.rect.x
            y_before = b.rect.y
            b.update(x, y)
            x = x_before
            y = y_before
        
        #print(list(map(lambda b: (b.rect.x, b.rect.y), self.body.sprites())))

        self.x += self.velocity[0]
        self.y += self.velocity[1]

    def read_keys(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.velocity = (-10, 0)
        if keys[pygame.K_RIGHT]:
            self.velocity = (10, 0)
        if keys[pygame.K_UP]:
            self.velocity = (0, -10)
        if keys[pygame.K_DOWN]:
            self.velocity = (0, 10)

    def grow_body(self):
        if len(self.sprites()) == 0:
            x = self.x
            y = self.y
        else:
            last = self.sprites()[-1]
            x = last.rect.x
            y = last.rect.y

        new_body = Body(x, y)
        self.add(new_body)
import pygame
from pygame.sprite import Sprite, Group, spritecollideany, groupcollide
from pygame.image import load
from pygame.transform import scale
from .utils import get_edges, Point

SNAKE_BLOCK = 12

class Direction:
    LEFT = Point(-SNAKE_BLOCK, 0)
    RIGTH = Point(SNAKE_BLOCK, 0)
    UP = Point(0, -SNAKE_BLOCK)
    DOWN = Point(0, SNAKE_BLOCK)

class Head(Sprite):
    def __init__(self, pos: Point):
        super().__init__()

        self.image = scale(
            load('images/snake.png'),
            (SNAKE_BLOCK, SNAKE_BLOCK)
        )
        self.image.get_offset
        self.rect = self.image.get_rect(
            center=pos
        )
        self.velocity = Point(SNAKE_BLOCK, 0)

    @property
    def pos(self):
        return Point(self.rect.x, self.rect.y)
    
    def update(self):
        self.read_keys()
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

    def read_keys(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.velocity != Direction.RIGTH:
            self.velocity = Direction.LEFT
        if keys[pygame.K_RIGHT] and self.velocity != Direction.LEFT:
            self.velocity = Direction.RIGTH
        if keys[pygame.K_UP] and self.velocity != Direction.DOWN:
            self.velocity = Direction.UP
        if keys[pygame.K_DOWN] and self.velocity != Direction.UP:
            self.velocity = Direction.DOWN

class Body(Sprite):
    def __init__(self, pos: Point):
        super().__init__()

        self.image = scale(
            load('images/snake.png'),
            (SNAKE_BLOCK, SNAKE_BLOCK)
        )
        self.rect = self.image.get_rect(
            center=pos
        )

    def update(self, pos):
        self.rect.x = pos.x
        self.rect.y = pos.y

    @property
    def pos(self):
        return Point(self.rect.x, self.rect.y)
        

class Snake(Group):
    def __init__(self, game):
        super().__init__()

        self.game = game
        self.map = game.map
        head_pos = Point(
            x = game.map.surface.get_width() / 2,
            y = game.map.surface.get_height() / 2
        )
        self.head = Head(head_pos)
        self.bodyGroup = Group(Body(self.head.pos + Point(-SNAKE_BLOCK, 0)))
        self.add(self.head)

    @property
    def body(self):
        return self.bodyGroup.sprites()

    def update(self):
        self.manage_collisions()
        self.head.update()
        self.update_body()

    def draw(self, surface: pygame.Surface):
        self.bodyGroup.draw(surface)
        super().draw(surface)

    def update_body(self):
        pos = self.head.pos

        for b in self.body:
            pos_before = b.pos
            b.update(pos)
            pos = pos_before
            
    def manage_collisions(self):
        if self.has_collision() or self.has_collision_self():
            self.game.end_game()

    def has_collision_self(self):
        count = 0
        for head, bodies in groupcollide(self, self.bodyGroup, False, False).items():
            if len(bodies) > 1:
                return True
        return False

    def has_collision(self):
        return len(list(filter(self.check_collision, get_edges(self.head)))) > 0

    def check_collision(self, point):
        return not self.map.is_within_map(point) or self.map.is_infected(point)

    def grow_body(self):
        self.bodyGroup.add(Body(Point(0, 0)))
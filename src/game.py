import pygame
import random
from pygame import QUIT, Color, display, Surface
from pygame import event
from floodfill import dsf_flood_fiil
from point import Point
from pygame.transform import scale
from pygame.image import load
from pygame.sprite import Sprite, GroupSingle
from snake import Snake
from pygame.time import Clock

pygame.init()

size = 800, 600
pos_game = (105, 70)
size_game = (590, 430)

surface = display.set_mode(size=size)
game_surface = Surface(size_game, pygame.SRCALPHA, 32)
GAME_DEFAULT_COLOR = Color(0, 0, 0, 0)
START_FLOOD_FILL = [Point(100, 120), Point(450, 400)]


display.set_caption("SnakeFloodFill")

background = scale(
    load("../images/background.png"),
    size
)

snake = Snake(400, 400)
snake_group = GroupSingle(snake)

floods = [
    dsf_flood_fiil(random.choice(START_FLOOD_FILL), game_surface, Color(10, 200, 255)),
    dsf_flood_fiil(random.choice(START_FLOOD_FILL), game_surface, Color(10, 200, 255)),
]

clock = Clock()

lost = False

def has_lost(snake: Sprite, surface: Surface, pos_game):
    snakeX, snakeY = snake.rect.x, snake.rect.y
    snakeWidth, snakeHeigth = snake.rect.width, snake.rect.height

    if snakeX <= pos_game[0] or snakeX + snakeWidth > surface.get_width() + pos_game[0]:
        return True
    if snakeY <= pos_game[1] or snakeY + snakeHeigth > surface.get_height() + pos_game[1]:
        return True
    return surface.get_at((snakeX-pos_game[0], snakeY-pos_game[1])) != GAME_DEFAULT_COLOR

while not lost:
    # Loop de eventos

    clock.tick(120)  # FPS

    for flood in floods:
        try:
            for _ in range(10):
                next(flood)
        except StopIteration:
            floods.remove(flood)

    # Espaço dos eventos
    for evento in event.get():  # Events
        if evento.type == QUIT:
            pygame.quit()


    surface.blit(background, (0, 0))
    surface.blit(game_surface, pos_game)

    snake_group.draw(surface)
    snake_group.update()

    lost = has_lost(snake_group.sprite, game_surface, pos_game)

    display.update()

print("Perdeu!!!")
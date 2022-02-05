import pygame
import random
from pygame import QUIT, Color, display, Surface, event, font
from floodfill import bsf_flood_fill, dsf_flood_fill
from point import Point
from pygame.transform import scale
from pygame.image import load
from pygame.sprite import Sprite, GroupSingle, groupcollide
from snake import Snake
from fruit import Fruit
from pygame.time import Clock

SIZE = 800, 600
POS_GAME = (105, 70)
SIZE_GAME = (590, 430)

GAME_DEFAULT_COLOR = Color(0, 0, 0, 0)
START_FLOOD_FILL = [Point(1, 1), Point(589, 429), Point(439, 150)]

pygame.init()

#Display settings
surface = display.set_mode(size=SIZE)
game_surface = Surface(SIZE_GAME, pygame.SRCALPHA, 32)
display.set_caption("SnakeFloodFill")
background = scale(
    load("../images/background.png"),
    SIZE
)
clock = Clock()

#Fonts settings
game_over_font = font.SysFont('roboto', 100)
score_font = font.SysFont('roboto', 40)

#Snake settings
snake = Snake(400, 400)
lost = False
points = 0

#Floods
floods = [
    bsf_flood_fill(random.choice(START_FLOOD_FILL), game_surface, Color(10, 200, 255)),
    dsf_flood_fill(random.choice(START_FLOOD_FILL), game_surface, Color(10, 200, 255)),
    bsf_flood_fill(random.choice(START_FLOOD_FILL), game_surface, Color(10, 200, 255)),
    dsf_flood_fill(random.choice(START_FLOOD_FILL), game_surface, Color(10, 200, 255)),
]

def has_lost(snake: Sprite, surface: Surface, pos_game):
    snakeX, snakeY = snake.rect.x, snake.rect.y
    snakeWidth, snakeHeigth = snake.rect.width, snake.rect.height

    if snakeX <= pos_game[0] or snakeX + snakeWidth > surface.get_width() + pos_game[0]:
        return True
    if snakeY <= pos_game[1] or snakeY + snakeHeigth > surface.get_height() + pos_game[1]:
        return True
    return is_infected(snake)

def is_infected(object: Sprite):
    return game_surface.get_at((object.rect.x-POS_GAME[0], object.rect.y-POS_GAME[1])) != GAME_DEFAULT_COLOR

fruit = Fruit(is_infected, game_surface, POS_GAME)
fruit_group = GroupSingle(fruit)

while not lost:
    # Loop de eventos
    clock.tick(15)  # FPS

    surface.blit(background, (0, 0))
    surface.blit(game_surface, POS_GAME)

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

    snake.update()
    snake.draw(surface)

    fruit_group.update()
    fruit_group.draw(surface)

    lost += has_lost(snake.sprites()[0], game_surface, POS_GAME)

    if groupcollide(snake, fruit_group, False, True):
        points += 1
        snake.grow_body()
        fruit2 = Fruit(is_infected, game_surface, POS_GAME)
        fruit_group.add(fruit2)

    score = score_font.render(
        f"Points: {points}",
        True,
        (0, 0, 0)
    )
    surface.blit(score, (340, 550))

    if (lost):
        game_over = game_over_font.render(
            "Game Over!",
            True,
            (255, 255, 255)
        )

        final_score = score_font.render(
            f"Final Score: {points}",
            True,
            (255, 255, 255)
        
        )
        surface.blit(game_over, (200, 200))
        surface.blit(final_score, (330, 270))

        display.update()
        pygame.time.delay(4500)
    

    display.update()
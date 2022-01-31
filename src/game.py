import pygame
from pygame import QUIT, Color, display, Surface
from pygame import event
from floodfill import dsf_flood_fiil
from point import Point
from pygame.transform import scale
from pygame.image import load


pygame.init()

size = 800, 600
pos_game = (105, 70)
size_game = (590, 430)

surface = display.set_mode(size=size)
game_surface = Surface(size_game, pygame.SRCALPHA, 32)

display.set_caption("SnakeFloodFill")

background = scale(
    load("../images/background.png"),
    size
)

floods = [
    dsf_flood_fiil(Point(400, 300), game_surface, Color(255, 255, 255)),
    dsf_flood_fiil(Point(100, 300), game_surface, Color(0, 255, 255)),
    dsf_flood_fiil(Point(200, 300), game_surface, Color(255, 0, 255)),
]

while True:
    # Loop de eventos

    for flood in floods:
        try:
            for _ in range(500):
                next(flood)
        except StopIteration:
            floods.remove(flood)

    # Espaço dos eventos
    for evento in event.get():  # Events
        if evento.type == QUIT:
            pygame.quit()


    surface.blit(background, (0, 0))
    surface.blit(game_surface, pos_game)

    display.update()

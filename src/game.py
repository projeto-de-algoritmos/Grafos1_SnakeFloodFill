import pygame
from pygame import QUIT, Color, display
from pygame import event
from floodfill import dsf_flood_fiil
from point import Point

pygame.init()

tamanho = 800, 600
superficie = display.set_mode(size=tamanho)
display.set_caption("SnakeFloodFill")

floods = [
    dsf_flood_fiil(Point(400, 300), superficie, Color(255, 255, 255)),
    dsf_flood_fiil(Point(0, 0), superficie, Color(255, 0, 255)),
    dsf_flood_fiil(Point(tamanho[0]-1, tamanho[1]-1), superficie, Color(100, 100, 255)),
    dsf_flood_fiil(Point(0, tamanho[1]-1), superficie, Color(255, 0, 0)),
]

while True:
    # Loop de eventos

    for flood in floods:
        try:
            for _ in range(20):
                next(flood)
        except StopIteration:
            floods.remove(flood)

    # Espaço dos eventos
    for evento in event.get():  # Events
        if evento.type == QUIT:
            pygame.quit()

    display.update()

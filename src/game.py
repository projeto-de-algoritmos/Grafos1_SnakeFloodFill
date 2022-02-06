import pygame
from pygame import QUIT, display, event
from pygame.surface import Surface
from pygame.time import Clock
from pygame.sprite import AbstractGroup
from .config import GameConfig

GameObject = AbstractGroup


class GameSurface(GameObject):
    def __init__(self, surface: Surface):
        self.objects: list[GameObject] = []
        self.surface = surface

    def add_object(self, object: GameObject):
        self.objects.append(object)

    def remove_object(self, object: GameObject):
        self.objects.remove(object)

    def update(self):
        for obj in self.objects:
            try:
                obj.update()
            except RemoveGameObject:
                self.remove_object(obj)

    def draw(self, surface: Surface):
        for obj in self.objects:
            obj.draw(surface)


class Game(GameSurface):
    def __init__(self, config: GameConfig):
        super().__init__(display.set_mode(size=config.window_size))
        pygame.init()
        play_music(config.music)
        display.set_caption(config.title)

        self.config = config
        self.running = False
        self.clock = Clock()

    @property
    def size(self):
        return self.config.window_size

    def run(self):
        self.running = True
        self._run()

    def _run(self):
        while self.running:
            self.clock.tick(self.config.fps)

            self.update()
            self.draw()

            self.manage_events()

            display.update()

    def manage_events(self):
        for evento in event.get():
            if evento.type == QUIT:
                self.end()

    def end(self):
        self.running = False

    def draw(self):
        super().draw(self.surface)

def play_music(music: str):
    pygame.mixer.music.load(music)
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

class RemoveGameObject(Exception):
    ...

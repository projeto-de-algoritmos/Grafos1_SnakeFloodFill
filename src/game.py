import pygame
from pygame import QUIT, Surface, display, event
from pygame.time import Clock
from pygame.sprite import AbstractGroup
from typing import Protocol

class GameObject(Protocol):
    def update(self):
        ...

    def draw(self, surface: Surface):
        ...

class Game:
    def __init__(self, title: str, width:int, height: int, fps: int = 120):
        pygame.init()
        display.set_caption(title)

        self.width = width
        self.height = height
        self.running = False
        self.fps = fps
        self.clock = Clock()
        self.surface = display.set_mode(size=(width, height))
        self.objects: list[GameObject] = []

    @property
    def size(self):
        return (self.width, self.height)
      
    def add_object(self, object: GameObject):
        self.objects.append(object)
    
    def remove_object(self, object: GameObject):
        self.objects.remove(object)

    def run(self):
        self.running = True
        self._run()

    def _run(self):
        while self.running:
            self.clock.tick(self.fps)
            
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

    def update(self):
        for obj in self.objects:
            obj.update()

    def draw(self):
        for obj in self.objects:
            obj.draw(self.surface)
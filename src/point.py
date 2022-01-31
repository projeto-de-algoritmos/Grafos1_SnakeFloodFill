from dataclasses import dataclass
from typing import Tuple

@dataclass
class Point:
    x: int
    y: int

    def get(self) -> Tuple[int, int]:
        return (self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
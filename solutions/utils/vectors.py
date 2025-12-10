from dataclasses import dataclass
import unittest

@dataclass(frozen=True)
class Point():
    x: int
    y: int

    def getRectArea(self, other) -> int:
        # Area of a rectangle from opposite corners
        return (abs(self.x - other.x) + 1) * (abs(self.y - other.y) + 1)

    def __sub__(self, other) -> int:
        # Euclidian Distance
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

class Vector():
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
        self.x = end.x - start.x
        self.y = end.y - start.y
        self.magnitude = sqrt(self.x**2 + self.y**2)

    def __len__(self):
        return self.magnitude


    #cross product self x other
    def __mul__(self, other) -> int:
        return self.x * self.y - self.y * self.x

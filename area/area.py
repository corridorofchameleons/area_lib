import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        raise NotImplementedError


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def is_right(self):
        sorted_sides = sorted([self.a, self.b, self.c], reverse=True)
        return sorted_sides[0] ** 2 == sorted_sides[1] ** 2 + sorted_sides[2] ** 2


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * (self.r ** 2)

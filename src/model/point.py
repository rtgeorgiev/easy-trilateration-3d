from math import hypot


class Point:
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        self.x = x_init
        self.y = y_init

    def __repr__(self):
        return "".join(["Point(", str(self.x), ",", str(self.y), ")"])

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Point):
            return (self.x == other.x) & (self.y == other.y)
        return False

    def __hash__(self):
        return hash(str(self))

    def shift(self, x, y):
        self.x += x
        self.y += y

    def sum(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def subtract(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def multiply(self, factor):
        return Point(self.x * factor, self.y * factor)

    def distance(self, b):
        return hypot(self.x - b.x, self.y - b.y)

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


class Circle:
    center: Point
    radius: float

    def __init__(self, x: float, y: float, r: float):
        self.center = Point(x, y)
        self.radius = r

    def __repr__(self):
        return "".join(["Circle(", str(self.center.x), ", ", str(self.center.y), ", ", str(self.radius), ")"])

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Circle):
            return (self.center.x == other.center.x) & (self.center.y == other.center.y) & (self.radius == other.radius)
        return False


def find_intersections(circles: [Circle]):
    ret = set()
    for item in circles:
        for item2 in circles:
            if item.intersects(item2):
                for item3 in item.get_intersection_points(item2):
                    print("intersects on " + str(item3))
                    ret.add(item3)
    return ret


class Trilateration:
    sniffers: [Circle]
    result: Circle

    def __init__(self, sniffers: [Circle], result: Circle = None):
        self.sniffers = sniffers
        self.result = result

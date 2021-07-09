from math import sqrt, hypot


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

    def __init__(self, point_init: Point, r_init: float):
        self.center = point_init
        self.radius = r_init

    def __repr__(self):
        return "".join(["Circle(", str(self.center.x), ", ", str(self.center.y), ", ", str(self.radius), ")"])

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Circle):
            return (self.center.x == other.center.x) & (self.center.y == other.center.y) & (self.radius == other.radius)
        return False

    def shift(self, x, y):
        self.center.shift(x, y)

    def shift_radius(self, r):
        self.radius += r

    def has_inside(self, point: Point):
        return self.center.distance(point) <= self.radius

    def intersects(self, other):
        if not isinstance(other, Circle):  # if not a circle
            return False
        if self.center.distance(other.center) > (self.radius + other.radius):
            return False  # They dont intersect
        elif self.center.distance(other.center) < abs(self.radius - other.radius):
            return False  # One is inside the other
        elif (self.center.distance(other.center) == 0) and (self.radius == other.radius):
            return False  # They are exactly the same circle
        else:  # if distance(a.center,b.center)<=a.r+b.r
            return True

    def distance_to_intersection(self, other):
        if not isinstance(other, Circle):  # if not a circle
            return None
        return self.center.distance(other.center) - (self.radius + other.radius)

    def get_intersection_points(self, other, precision: int = None):
        if not self.intersects(other):
            return {}

        distance_between_centers = self.center.distance(other.center)
        if precision is not None:
            distance_between_centers = round(distance_between_centers, precision)

        distance_between_x = other.center.x - self.center.x
        distance_between_y = other.center.y - self.center.y
        distance_center_to_middle = (self.radius ** 2 - other.radius ** 2 + distance_between_centers ** 2) / (
                2 * distance_between_centers)
        distance_between_intersection_points = sqrt(self.radius ** 2 - distance_center_to_middle ** 2)
        intersection_center_x = self.center.x + (
                distance_center_to_middle * distance_between_x / distance_between_centers)
        intersection_center_y = self.center.y + (
                distance_center_to_middle * distance_between_y / distance_between_centers)

        intersection_point_a_x = intersection_center_x + (
                distance_between_intersection_points * distance_between_y) / distance_between_centers
        intersection_point_a_y = intersection_center_y - (
                distance_between_intersection_points * distance_between_x) / distance_between_centers
        if precision is not None:
            intersection_point_a_x = round(intersection_point_a_x, precision)
            intersection_point_a_y = round(intersection_point_a_y, precision)
        intersection_point_a = Point(intersection_point_a_x, intersection_point_a_y)

        intersection_point_b_x = intersection_center_x - (
                distance_between_intersection_points * distance_between_y) / distance_between_centers
        intersection_point_b_y = intersection_center_y + (
                distance_between_intersection_points * distance_between_x) / distance_between_centers
        if precision is not None:
            intersection_point_b_x = round(intersection_point_b_x, precision)
            intersection_point_b_y = round(intersection_point_b_y, precision)
        intersection_point_b = Point(intersection_point_b_x, intersection_point_b_y)

        return {intersection_point_a, intersection_point_b}


def find_intersections(circles: [Circle]):
    ret = set()
    for item in circles:
        for item2 in circles:
            if item.intersects(item2):
                for item3 in item.get_intersection_points(item2):
                    print("intersects on " + str(item3))
                    ret.add(item3)
    return ret
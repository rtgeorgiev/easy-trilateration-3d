class Point:
    x: float
    y: float
    z: float  # New attribute for z-coordinate

    def __init__(self, x_init: float, y_init: float, z_init: float):
        self.x = x_init
        self.y = y_init
        self.z = z_init

    def __repr__(self):
        return f"Point({self.x}, {self.y}, {self.z})"

    def __eq__(self, other):
        if isinstance(other, Point):
            return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)
        return False

    def __hash__(self):
        return hash((self.x, self.y, self.z))


class Circle:
    center: Point
    radius: float

    def __init__(self, x: float, y: float, z: float, r: float):
        self.center = Point(x, y, z)  # Store a 3D point as the center
        self.radius = r

    def __repr__(self):
        return f"Circle(center={self.center}, radius={self.radius})"

    def __eq__(self, other):
        if isinstance(other, Circle):
            return (self.center == other.center) and (self.radius == other.radius)
        return False


class Trilateration:
    sniffers: [Circle]
    result: Circle
    meta: float  # or any appropriate data type

    def __init__(self, sniffers: [Circle], result: Circle = None, meta: float = None):
        self.sniffers = sniffers
        self.result = result
        self.meta = meta

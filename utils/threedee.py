from math import sqrt


class Vec3i:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance_to_sqrt(self, other) -> int:
        return ((self.x - other.x)**2 + (self.y - other.y)**2) + (self.z - other.z)**2

    @staticmethod
    def parse(s: str):
        return Vec3i(*map(int, s.split(",")))

    __str__ = lambda self: f"Vec3i(x:{self.x}, y:{self.y}, z:{self.z})"
    __repr__ = lambda self: str(self)
    __hash__ = lambda self: hash((self.x, self.y, self.z))

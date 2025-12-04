from typing import TypeVar, Generic, Callable


class Vec2i:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Vec2i(x:{self.x}, y:{self.y})"

    def __add__(self, other):
        return Vec2i(self.x + other.x, self.y + other.y)

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))


T = TypeVar('T')


class Map2d(Generic[T]):
    @staticmethod
    def create(w: int, h: int, initialData: T) -> Map2d[T]:
        data = []
        for y in range(h):
            row = []
            for x in range(w):
                row.append(initialData)
            data.append(row)
        return Map2d(data)

    def __init__(self, data: list[list[T]]) -> None:
        self.data = data
        self.width = len(self.data[0])
        self.height = len(self.data)

    def __getitem__(self, pos: Vec2i) -> T:
        return self.data[pos.y][pos.x]

    def __setitem__(self, pos: Vec2i, value: T) -> None:
        self.data[pos.y][pos.x] = value

    def get_neighbors(self, pos: Vec2i) -> list[Vec2i]:
        result = []
        for p in (
                Vec2i(-1, -1),
                Vec2i(0, -1),
                Vec2i(1, -1),
                Vec2i(-1, 0),
                Vec2i(1, 0),
                Vec2i(-1, 1),
                Vec2i(0, 1),
                Vec2i(1, 1)
        ):
            neighborPos = pos + p
            if self.contains(neighborPos):
                result.append(neighborPos)
        return result

    def get_positions_of(self, selector: Callable[[T], bool]) -> list[Vec2i]:
        result = []
        for y in range(self.height):
            for x in range(self.width):
                pos = Vec2i(x, y)
                data = self[pos]
                if selector(data):
                    result.append(pos)
        return result

    def contains(self, pos: Vec2i) -> bool:
        return 0 <= pos.x < self.width and 0 <= pos.y < self.height

    def __str__(self) -> str:
        result = ''
        for row in self.data:
            result += str(''.join(row)) + '\n'
        return result

from AocUtils import read_file_as_2d_array
from utils.twodee import Map2d, Vec2i

class Task:
    def __init__(self, input_file):
        self.map = Map2d(read_file_as_2d_array(input_file))

    def solve_part1(self):
        rollPositions = self.map.get_positions_of(lambda d: '@' == d)

        moveable = list()
        for rollPosition in rollPositions:
            c = self.count_neighbor_rolls(rollPosition)
            if 4 > c:
                moveable.append(rollPosition)

        return len(moveable)

    def count_neighbor_rolls(self, pos) -> int:
        directions = (
            Vec2i(-1, -1),
            Vec2i(0, -1),
            Vec2i(1, -1),
            Vec2i(-1, 0),
            Vec2i(1, 0),
            Vec2i(-1, 1),
            Vec2i(0, 1),
            Vec2i(1, 1),
        )

        numNeighborRolls = 0
        for direction in directions:
            c = pos + direction
            if self.map.contains(c) and '@' == self.map[c]:
                numNeighborRolls += 1

        return numNeighborRolls

    def solve_part2(self):
        removedTotal = 0
        removed = 1
        rollPositions = self.map.get_positions_of(lambda d: '@' == d)
        while 0 < removed:
            moveable = list()
            for rollPosition in rollPositions:
                c = self.count_neighbor_rolls(rollPosition)
                if 4 > c:
                    moveable.append(rollPosition)

            removed = len(moveable)
            if 0 < removed:
                removedTotal += removed
                for p in moveable:
                    self.map[p] = 'x'
                    rollPositions.remove(p)

        return removedTotal


def run(path):
    uut = Task(path + '/example.txt')
    result = uut.solve_part1()
    print("Part 1 (example) result: " + str(result))

    uut = Task(path + '/input.txt')
    result = uut.solve_part1()
    print("Part 1 (input) result: " + str(result))

    uut = Task(path + '/example.txt')
    result = uut.solve_part2()
    print("Part 2 (example) result: " + str(result))

    uut = Task(path + '/input.txt')
    result = uut.solve_part2()
    print("Part 2 (input) result: " + str(result))


if __name__ == '__main__':
    run(".")

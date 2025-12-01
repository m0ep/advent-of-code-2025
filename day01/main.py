import re

class Lock:
    def __init__(self, value: int):
        self.value = value

    def __str__(self):
        return "Lock(" + str(self.value) + ")"

    def apply(self, turn: Turn):
        direction = 1 if turn.direction == 'R' else -1
        dist = turn.distance
        zero_count = 0
        while 0 < dist:
            self.value += direction
            dist -= 1

            if 100 == self.value:
                self.value = 0
            elif -1 == self.value:
                self.value = 99

            if 0 == self.value:
                zero_count += 1

        return zero_count

class Turn:
    def __init__(self, direction: str, distance: int):
        self.direction = direction
        self.distance = distance

    def __str__(self):
        return "Turn(" + self.direction + ", " + str(self.distance) + ")"

class Day01:
    def __init__(self, input_file):
        with open(input_file) as f:
            self.input_lines = [line.rstrip() for line in f]

    def solve_part1(self):
        lock = Lock(50)
        turns = self.parse_turns()

        zero_count = 0
        for turn in turns:
            lock.apply(turn)
            if 0 == lock.value:
                zero_count += 1

        return zero_count

    def parse_turns(self) -> list[Any]:
        turns = list()
        for line in self.input_lines:
            match = re.match("[RL][0-9]+", line)
            if match:
                turns.append(Turn(match.group(0)[0], int(match.group(0)[1:])))
        return turns

    def solve_part2(self):
        lock = Lock(50)
        turns = self.parse_turns()

        zero_count = 0
        for turn in turns:
            zero_count += lock.apply(turn)

        return zero_count

def run(path):
    uut = Day01(path + '/example.txt')
    result = uut.solve_part1()
    print("Part 1 (example) result: " + str(result))

    uut = Day01(path + '/input.txt')
    result = uut.solve_part1()
    print("Part 1 (input) result: " + str(result))

    uut = Day01(path + '/example.txt')
    result = uut.solve_part2()
    print("Part 2 (example) result: " + str(result))

    uut = Day01(path + '/input.txt')
    result = uut.solve_part2()
    print("Part 2 (input) result: " + str(result))

if __name__ == '__main__':
    run(".")
import re


class Task:
    def __init__(self, input_file):
        with open(input_file) as f:
            self.input_lines = [line for line in f.read().splitlines()]
            print(self.input_lines)

    def solve_part1(self):
        return 0

    def solve_part2(self):
        return 0


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

import re


class Day01Part1:
    def __init__(self, input_file):
        with open(input_file) as f:
            self.input_lines = [line.rstrip() for line in f]

    def solve(self):
        print(self.input_lines)

        for line in self.input_lines:
            match = re.match("[RL][0-9]+", line)
            if(match):
                print(match.group(0)[0] + " -> " + match.group(0)[1:])


if __name__ == '__main__':
    print('Example: ')
    part1 = Day01Part1('example.txt')
    part1.solve()

    print('Input: ')
    part1 = Day01Part1('input.txt')
    part1.solve()
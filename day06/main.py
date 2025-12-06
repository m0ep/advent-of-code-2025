import re
from functools import reduce
from typing import List


class Problem:

    def __init__(self, numbers: List[str], operation: str):
        self.numbers: list[str] = numbers
        self.operation: str = operation.strip()

    def solve(self):
        if '+' == self.operation:
            opFunc = lambda x, y: x + y
            initial = 0
        elif '*' == self.operation:
            opFunc = lambda x, y: x * y
            initial = 1
        else:
            return 0

        return reduce(opFunc, map(int, self.numbers), initial)

    def __str__(self):
        return f"Problem(numbers={self.numbers}, operation={self.operation})"

    def __repr__(self):
        return str(self)

class Task:
    def __init__(self, input_file):
        self.problemColumns: list[list[str]] = []
        with open(input_file) as f:
            data = [line.rstrip('\n') for line in f.read().splitlines()]
            operatorsLine = data[-1]

            starIdx = []
            operators = []

            buffer = None
            for i,c in enumerate(operatorsLine):
                if c in ['+','*']:
                    if buffer is None:
                        starIdx.append(i)
                        buffer = c
                    else:
                        if buffer[-1] == ' ':
                            buffer = buffer[:-1]
                        operators.append(buffer.strip())
                        starIdx.append(i)
                        buffer = c

                    if i == len(operatorsLine)-1:
                        operators.append(buffer.strip())
                elif '\n' == c:
                    operators.append(buffer.strip())
                    buffer = None
                else:
                    buffer += c

            self.problemColumns = []
            for i in range(len(starIdx)):
                self.problemColumns.append([])

            for dataLine in data:
                for idx in range(len(starIdx)-1):
                    number = dataLine[starIdx[idx]:starIdx[idx+1]-1]
                    self.problemColumns[idx].append(number)

                self.problemColumns[len(starIdx)-1].append(dataLine[starIdx[-1]:])

    def solve_part1(self):
        result = 0
        for problemColumns in self.problemColumns:
            problem = Problem(problemColumns[:-1], problemColumns[-1])
            result += problem.solve()

        return result

    def solve_part2(self):
        result = 0

        for problemColumns in self.problemColumns:
            numbersRaw = problemColumns[:-1]
            operations = problemColumns[-1]
            maxNumCols = max(map(len, numbersRaw))

            numbers = []
            for numRaw in numbersRaw:
                if len(numRaw) < maxNumCols:
                    numRaw = numRaw.ljust(maxNumCols, ' ')

                for i in range(maxNumCols):
                    if i >= len(numbers):
                        numbers.append([])

                    if ' ' != numRaw[i]:
                     numbers[i].append(numRaw[i])

            numbers = ([(''.join(n)) for n in numbers])
            numbers.reverse()

            problem = Problem(numbers, operations.strip())
            solve = problem.solve()
            result += solve

        return result


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
    #
    uut = Task(path + '/input.txt')
    result = uut.solve_part2()
    print("Part 2 (input) result: " + str(result))


if __name__ == '__main__':
    run(".")

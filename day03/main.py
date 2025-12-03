import re


class Task:
    def __init__(self, input_file):
        with open(input_file) as f:
            self.banks = [[int(x) for x in lint] for lint in f.read().splitlines()]

    def solve_part1(self):
        return self.calc_max_jolts(2)

    def calc_max_jolts(self, numBatteries: int) -> int:
        totalJolts = 0
        for bank in self.banks:
            result = list()
            leftIdx = 0
            while numBatteries > len(result):
                foundIdx = leftIdx
                for idx in range(leftIdx, len(bank) - (numBatteries - len(result) - 1)):
                    if bank[idx] > bank[foundIdx]:
                        foundIdx = idx

                result.append(bank[foundIdx])
                leftIdx = foundIdx + 1

            bankJolts = 0
            for idx in range(len(result)):
                bankJolts *= 10
                bankJolts += result[idx]
            totalJolts += bankJolts
        return totalJolts

    def solve_part2(self):
        return self.calc_max_jolts(12)

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

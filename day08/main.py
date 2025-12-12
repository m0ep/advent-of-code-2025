
from queue import PriorityQueue

from utils.threedee import Vec3i

## https://github.com/TheJP/AdventOfCode2025/blob/main/day08/

class Task:
    def __init__(self, input_file):
        self.points = list()
        with open(input_file) as f:
            for line in f.read().splitlines():
                pos = Vec3i.parse(line)
                self.points.append(pos)

        self.distanceQueue : PriorityQueue[tuple[int, int, int]] = PriorityQueue()
        for i in range(len(self.points)):
            p1 = self.points[i]
            for j in range(i+1, len(self.points)):
                p2 = self.points[j]
                dist = p1.distance_to_sqrt(p2)
                self.distanceQueue.put((dist, i, j))

    def solve_part1(self, firstN: int):

        circuitSize: list[int] = [1 for _ in range(len(self.points))]
        boxToCircuit: list[int] = [i for i in range(len(self.points))]

        selected: list[tuple[int, int]] = list()
        while not self.distanceQueue.empty():
            dist, idxFrom, idxTo = self.distanceQueue.get()
            selected.append((idxFrom, idxTo))

            if boxToCircuit[idxFrom] != boxToCircuit[idxTo]:
                c1 = boxToCircuit[idxFrom]
                c2 = boxToCircuit[idxTo]
                newCircuitSize = circuitSize[c1] + circuitSize[c2]
                newCircuitId = min(c1, c2)
                circuitSize[newCircuitId] = newCircuitSize
                circuitSize[max(c1, c2)] = 0

                for i in range(len(self.points)):
                    if boxToCircuit[i] == c1 or boxToCircuit[i] == c2:
                        boxToCircuit[i] = newCircuitId

            if len(selected) == firstN:
                break

        result = 1
        for s in sorted(circuitSize, reverse=True)[:3]:
            result *= s

        return result

    def solve_part2(self):
        circuitSize: list[int] = [1 for _ in range(len(self.points))]
        boxToCircuit: list[int] = [i for i in range(len(self.points))]

        numBoxes = len(self.points)
        selected: list[tuple[int, int]] = list()

        while not self.distanceQueue.empty():
            dist, idxFrom, idxTo = self.distanceQueue.get()
            selected.append((idxFrom, idxTo))

            if boxToCircuit[idxFrom] != boxToCircuit[idxTo]:
                c1 = boxToCircuit[idxFrom]
                c2 = boxToCircuit[idxTo]
                newCircuitSize = circuitSize[c1] + circuitSize[c2]
                newCircuitId = min(c1, c2)
                circuitSize[newCircuitId] = newCircuitSize
                circuitSize[max(c1, c2)] = 0

                for i in range(len(self.points)):
                    if boxToCircuit[i] == c1 or boxToCircuit[i] == c2:
                        boxToCircuit[i] = newCircuitId

                if newCircuitSize == numBoxes:
                    break

        lastPair = selected[-1]
        return self.points[lastPair[0]].x * self.points[lastPair[1]].x


def run(path):
    uut = Task(path + '/example.txt')
    result = uut.solve_part1(10)
    print("Part 1 (example) result: " + str(result))

    uut = Task(path + '/input.txt')
    result = uut.solve_part1(1000)
    print("Part 1 (input) result: " + str(result))

    uut = Task(path + '/example.txt')
    result = uut.solve_part2()
    print("Part 2 (example) result: " + str(result))

    uut = Task(path + '/input.txt')
    result = uut.solve_part2()
    print("Part 2 (input) result: " + str(result))


if __name__ == '__main__':
    run(".")

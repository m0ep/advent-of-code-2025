class IdRange:
    def __init__(self, start, end):
        self.startInclusive = start
        self.endInclusive = end

    def __str__(self):
        return f'{self.startInclusive}-{self.endInclusive}'

    def __repr__(self):
        return f'{self.startInclusive}-{self.endInclusive}'

    def to_range(self):
        return range(self.startInclusive, self.endInclusive + 1)

    def contains(self, value: int) -> bool:
        return self.startInclusive <= value <= self.endInclusive

    def overlaps(self, other: IdRange) -> bool:
        return (other.contains(self.startInclusive)
                or other.contains(self.endInclusive)
                or self.contains(other.startInclusive))

class Task:
    def __init__(self, input_file):
        with open(input_file) as f:
            ranges_raw, ingredients_raw = f.read().split("\n\n")

        self.idRanges : list[IdRange] = list()
        for line in ranges_raw.splitlines():
            start, end = line.split("-")
            self.idRanges.append(IdRange(int(start), int(end)))

        self.ingredient = [int(item) for item in ingredients_raw.splitlines()]

    def solve_part1(self):
        count = 0
        for ingredient in self.ingredient:
            for idRange in self.idRanges:
                if ingredient in idRange.to_range():
                    count += 1
                    break

        return count

    def solve_part2(self):
        queue = list(self.idRanges)
        queue.sort(key=lambda x: x.startInclusive)

        merged = list()
        currentRange = queue.pop(0)
        while 0 < len(queue):
            nextRange = queue.pop(0)
            if currentRange.overlaps(nextRange) or 1 == abs(nextRange.startInclusive - currentRange.endInclusive):
                currentRange = IdRange(
                    min(currentRange.startInclusive, nextRange.startInclusive),
                    max(currentRange.endInclusive, nextRange.endInclusive)
                )
            else:
                merged.append(currentRange)
                currentRange = nextRange

        merged.append(currentRange)

        result = 0
        for r in merged:
            result += (r.endInclusive - r.startInclusive)+1

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

    uut = Task(path + '/input.txt')
    result = uut.solve_part2()
    print("Part 2 (input) result: " + str(result))


if __name__ == '__main__':
    run(".")

import re


class Task:
    def __init__(self, input_file):
        with open(input_file) as f:
            self.productIdRanges = list()
            for element in f.read().split(","):
                item_parts = element.split("-")
                self.productIdRanges.append((int(item_parts[0]), int(item_parts[1])))

            self.productIdRanges.sort(key=lambda x: x[0])

    @staticmethod
    def is_valid_id_part1(productId):
        productIdStr = str(productId)
        productIdLen = len(productIdStr)
        if 0 != productIdLen % 2:
            return True

        return productIdStr[0:productIdLen//2] != productIdStr[productIdLen//2:]

    def solve_part1(self):
        invalidProductIds = list()
        for productIdRange in self.productIdRanges:
            for productId in range(productIdRange[0], productIdRange[1]+1):
                if not self.is_valid_id_part1(productId):
                    invalidProductIds.append(productId)

        return sum(invalidProductIds)

    @staticmethod
    def is_valid_id_part2(productId):
        productIdStr = str(productId)
        productIdLen = len(productIdStr)

        for step in range(productIdLen // 2, 0, -1):
            if 0 == productIdLen % step:
                chunks = [ productIdStr[i:i+step] for i in range(0, productIdLen, step)]
                if len(chunks) == chunks.count(chunks[0]):
                    #print(productIdStr + " -> " + str(chunks))
                    return False

        return True

    def solve_part2(self):
        invalidProductIds = list()
        for productIdRange in self.productIdRanges:
            for productId in range(productIdRange[0], productIdRange[1] + 1):
                if not self.is_valid_id_part2(productId):
                    invalidProductIds.append(productId)

        return sum(invalidProductIds)


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

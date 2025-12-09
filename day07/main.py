import re
from collections import defaultdict

from AocUtils import read_file_as_2d_array
from utils.twodee import Map2d, Vec2i


class Task:
    def __init__(self, input_file):
        with open(input_file) as f:
            self.map = Map2d(read_file_as_2d_array(input_file))

    def solve_part1(self):
        print(self.map)

        current_layer: list[Vec2i] = [self.map.find_first('S')]
        if current_layer[0] is None:
            return 0

        layer = 0
        splits = 0
        while True:
            next_layer=[]

            while 0 < len(current_layer):
                beam_source = current_layer.pop()
                next_beam_pos = beam_source + Vec2i(0, 1)
                if self.map.contains(next_beam_pos):
                    if '.' == self.map[next_beam_pos]:
                        self.map[next_beam_pos] = '|'
                        next_layer.append(next_beam_pos)
                    elif '^' == self.map[next_beam_pos]:
                        splits += 1

                        left_beam_pos = next_beam_pos + Vec2i(-1, 0)
                        if left_beam_pos not in next_layer:
                            next_layer.append(left_beam_pos)
                            self.map[left_beam_pos] = '|'

                        right_beam_pos = next_beam_pos + Vec2i(1, 0)
                        if right_beam_pos not in next_layer:
                            next_layer.append(right_beam_pos)
                            self.map[right_beam_pos] = '|'

            layer += 1
            print(f'Layer {layer}: {splits}')
            print(self.map)
            print("========================")
            if 0 < len(next_layer):
                current_layer = next_layer
            else:
                return splits

    def solve_part2(self):
        start_pos = self.map.find_first('S')
        current_layer: list[Vec2i] = [start_pos]
        if current_layer[0] is None:
            return 0

        layer = 0

        dist = defaultdict(lambda: 0)
        dist[start_pos.x] = 1

        while True:
            next_layer = []
            next_dist = defaultdict(lambda: 0)
            while 0 < len(current_layer):
                beam_source = current_layer.pop()
                next_beam_pos = beam_source + Vec2i(0, 1)
                if self.map.contains(next_beam_pos):
                    if '.' == self.map[next_beam_pos]:
                        next_dist[next_beam_pos.x] += dist[beam_source.x]
                        next_layer.append(next_beam_pos)
                    elif '^' == self.map[next_beam_pos]:
                        left_beam_pos = next_beam_pos + Vec2i(-1, 0)
                        next_layer.append(left_beam_pos)
                        next_dist[left_beam_pos.x] += dist[beam_source.x]

                        right_beam_pos = next_beam_pos + Vec2i(1, 0)
                        next_layer.append(right_beam_pos)
                        next_dist[right_beam_pos.x] += dist[beam_source.x]

            layer += 1
            if 0 == len(next_layer):
                break

            current_layer = next_layer
            dist = next_dist

        return sum(dist.values())




def run(path):
    # uut = Task(path + '/example.txt')
    # result = uut.solve_part1()
    # print("Part 1 (example) result: " + str(result))
    #
    # uut = Task(path + '/input.txt')
    # result = uut.solve_part1()
    # print("Part 1 (input) result: " + str(result))

    uut = Task(path + '/example.txt')
    result = uut.solve_part2()
    print("Part 2 (example) result: " + str(result))

    #uut = Task(path + '/input.txt')
    #result = uut.solve_part2()
    #print("Part 2 (input) result: " + str(result))


if __name__ == '__main__':
    run(".")

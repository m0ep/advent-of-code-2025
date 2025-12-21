import sys

import matplotlib.pyplot as plt
from utils.twodee import Vec2i

lineWidth = 1

def part1(positions: list[Vec2i]) -> None:
    maxArea = 0
    maxIdx = list()

    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            area = tile_area(positions[i], positions[j])
            if maxArea < area:
                maxArea = area
                maxIdx = [i, j]

    pos1 = positions[maxIdx[0]]
    pos2 = positions[maxIdx[1]]

    print (f'Part 1 max area: {maxArea}, positions: {pos1}, {pos2}')

def tile_area(a: Vec2i, b: Vec2i) -> int:
    return (abs(a.x - b.x) + 1) * (abs(a.y - b.y) + 1)

def part2(positions: list[Vec2i]) -> None:

    numRedTiles = len(positions)
    for i in range(numRedTiles + 1) :
        start = positions[i % numRedTiles]
        end = positions[(i+1) % numRedTiles]
        plt.plot([start.x, end.x], [start.y, end.y], 'g-', linewidth=lineWidth)

    for pos in positions:
        plt.plot(pos.x, pos.y, 'rs', markersize=lineWidth)

    plt.show()

    print(line_intersect(Vec2i(0,0), Vec2i(10,10), Vec2i(5,10), Vec2i(0,10)))

def line_intersect(a1: Vec2i, a2: Vec2i, b1: Vec2i, b2: Vec2i) -> bool:
    denom = (b2.y - b1.y) * (a2.x - a1.x) - (b2.x - b1.x) * (a2.y - a1.y)
    if 0 == denom:
        return False

    ua = ((b2.x - b1.x) * (a1.y - b1.y) - (b2.y - b1.y) * (a1.x - b1.x)) / denom
    if 0 > ua or ua > 1:
        return False

    ub = ((a2.x - a1.x) * (a1.y - b1.y) - (a2.y - a1.y) * (a1.x - b1.x)) / denom
    if 0 > ub or ub > 1:
        return False

    return True

    # x1,y1 = p1
    # x2,y2 = p2
    # x3,y3 = p3
    # x4,y4 = p4
    # denom = (y4-y3)*(x2-x1) - (x4-x3)*(y2-y1)
    # if denom == 0: # parallel
    #     return None
    # ua = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / denom
    # if ua < 0 or ua > 1: # out of range
    #     return None
    # ub = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / denom
    # if ub < 0 or ub > 1: # out of range
    #     return None
    # x = x1 + ua * (x2-x1)
    # y = y1 + ua * (y2-y1)
    # return (x,y)

if __name__ == '__main__':
    file = "example.txt"
    #file = "input.txt"
    lines = open(file).readlines()

    redTilePositions: list[Vec2i] = []
    for line in lines:
        redTilePositions.append(Vec2i(*map(int, line.split(","))))

    #part1(redTilePositions)
    part2(redTilePositions)
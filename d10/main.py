from utils.utils import *


def get_neighbours(i, j, h, w):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    directions = [(i + dir[0], j + dir[1]) for dir in directions]
    return list(filter(lambda x: in_bounds(x[0], x[1], h, w), directions))


def find_hiketrails(grid, part_two=False):
    counter = 0
    h, w = len(grid), len(grid[0])
    for i, row in enumerate(grid):
        for j, head in enumerate(row):
            if head != 0:
                continue
            queue = [(i, j)]
            visited = set()
            while queue:
                node = queue.pop(0)
                if grid[node[0]][node[1]] == 9:
                    if not part_two and node in visited:
                         continue
                    visited.add(node)
                    counter += 1
                    continue
                neighbours = get_neighbours(node[0], node[1], h, w)
                for neighbour in neighbours:
                    if grid[neighbour[0]][neighbour[1]] - grid[node[0]][node[1]] == 1:
                        queue.append(neighbour)
    return counter  


def solution():
    lines = list(map(lambda x: list(map(lambda y: int(y), x)), get_lines('inputs/input10')))
    print(find_hiketrails(lines))
    print(find_hiketrails(lines, True))
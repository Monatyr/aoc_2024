from utils.utils import *


def get_fences_number(grid, i, j, h, w):
    counter = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dir in directions:
        y, x = i + dir[0], j + dir[1]
        if not in_bounds(y, x, h, w) or grid[i][j] != grid[y][x]:
            counter += 1
    return counter


def calculate_fence_cost_for_area(perimiter: int, area: int):
    return perimiter * area


def visit_field(grid, i, j, visited: list[list[bool]]):
    h, w = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    res = [(i, j)]
    visited[i][j] = True
    for dir in directions:
        y, x = i + dir[0], j + dir[1]
        if in_bounds(y, x, h, w) and not visited[y][x] and grid[i][j] == grid[y][x]:
            res.extend(visit_field(grid, y, x, visited))
    return res


def find_gardens(grid):
    visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
    gardens = list()
    for i, line in enumerate(grid):
        for j, el in enumerate(line):
            if not visited[i][j]:
                gardens.append(visit_field(grid, i, j, visited))
    return gardens


def calculate_fence_cost(grid, part_two=False):
    res = 0
    h, w = len(grid), len(grid[0])
    gardens = find_gardens(grid)
    for fields in gardens:
        if part_two:
            sides = get_sides_of_garden(grid, fields)
            res += len(fields) * sides
            continue
        number_of_fences = 0
        for field in fields:
            number_of_fences += get_fences_number(grid, field[0], field[1], h, w)
        res += number_of_fences * len(fields)
    return res


def find_group(groups, el, vertical=True):
    if len(groups) == 0:
        return None
    for group in groups:
        for cell in group:
            if vertical and abs(el[1] - cell[1]) == 1:
                return group
            if not vertical and abs(el[0] - cell[0]) == 1:
                return group
    return None


def get_sides_of_garden(grid, garden):
    res = 0
    h, w = len(grid), len(grid[0])
    vertical = [(-1, 0), (1, 0)]
    horizontal = [(0, -1), (0, 1)]
    for direction in vertical:
        min_index = min(garden, key=lambda x: x[0])[0]
        max_index = max(garden, key=lambda x: x[0])[0]
        for i in range(min_index, max_index + 1):
            groups = list()
            line = sorted(list(filter(lambda x: x[0] == i, garden)), key=lambda x: x[1])
            for el in line:
                y, x = el[0] + direction[0], el[1] + direction[1]
                if in_bounds(y, x, h, w) and grid[y][x] == grid[el[0]][el[1]]:
                    continue
                group = find_group(groups, el, True)
                if group is None:
                    group = set()
                    group.add(el)
                    groups.append(group)
                else:
                    group.add(el)
            res += len(groups)
    for direction in horizontal:
        min_index = min(garden, key=lambda x: x[1])[1]
        max_index = max(garden, key=lambda x: x[1])[1]
        for i in range(min_index, max_index + 1):
            groups = list()
            line = sorted(list(filter(lambda x: x[1] == i, garden)), key=lambda x: x[0])
            for el in line:
                y, x = el[0] + direction[0], el[1] + direction[1]
                if in_bounds(y, x, h, w) and grid[y][x] == grid[el[0]][el[1]]:
                    continue
                group = find_group(groups, el, False)
                if group is None:
                    group = set()
                    group.add(el)
                    groups.append(group)
                else:
                    group.add(el)
            res += len(groups)
    return res


def solution():
    lines = get_lines('inputs/input12')
    print(calculate_fence_cost(lines))
    print(calculate_fence_cost(lines, True))
    
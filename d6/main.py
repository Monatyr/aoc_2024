from utils.utils import *


def get_new_direction(old_direction: tuple[int, int]) -> tuple[int, int]:
    y_diff, x_diff = old_direction
    if y_diff == -1:
        return (0, 1)
    if x_diff == 1:
        return (1, 0)
    if y_diff == 1:
        return (0, -1)
    return (-1, 0)


def find_position(grid, symbol='^'):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == symbol:
                return (i, j)
    return None

# part 1
def get_distinct_positions(grid):
    h, w = len(grid), len(grid[0])
    y, x = find_position(grid)
    direction = (-1, 0)
    positions = set()
    while in_bounds(y, x, h, w):
        positions.add((y, x))
        new_y, new_x = y + direction[0], x + direction[1]
        if in_bounds(new_y, new_x, h, w):
            if grid[new_y][new_x] == '#':
                direction = get_new_direction(direction)
            else:
                y, x = new_y, new_x
        else:
            break
    return positions

# part 2
def count_potential_cycles(grid, distinct_positions: list):
    h, w = len(grid), len(grid[0])
    start_y, start_x = find_position(grid)
    distinct_positions.remove((start_y, start_x))
    res = 0
    for distinct_position in distinct_positions:
        grid[distinct_position[0]][distinct_position[1]] = '#'
        positions = set()
        direction = (-1, 0)
        y, x = start_y, start_x
        while in_bounds(y, x, h, w):
            if (y, x, direction) in positions: # cycle detected
                res += 1
                break
            positions.add((y, x, direction))
            new_y, new_x = y + direction[0], x + direction[1]
            if in_bounds(new_y, new_x, h, w):
                if grid[new_y][new_x] == '#':
                    direction = get_new_direction(direction)
                else:
                    y, x = new_y, new_x
            else:
                break
        grid[distinct_position[0]][distinct_position[1]] = '.'
    return res


def solution():
    grid = get_lines('inputs/input6')
    grid = list(map(lambda x: list(x), grid))
    distinct_positions = get_distinct_positions(grid)
    print(len(distinct_positions))
    print(count_potential_cycles(grid, distinct_positions))


from utils.utils import *


def parse_input(lines):
    res = []
    for line in lines:
        p, v = line.split()
        x, y = p.split(',')
        x, y = int(x[2:]), int(y)
        x_diff, y_diff = v.split(',')
        x_diff, y_diff = int(x_diff[2:]), int(y_diff)
        res.append([(y, x), (y_diff, x_diff)])
    return res


def count_robots_in_quadrants(robot_positions: list, h, w):
    res = 1
    mid_y, mid_x = h // 2, w // 2
    quadrant_ranges = [
        (range(0, mid_y), range(0, mid_x)),
        (range(0, mid_y), range(mid_x + 1, w)),
        (range(mid_y + 1, h), range(0, mid_x)),
        (range(mid_y + 1, h), range(mid_x + 1, w))
    ]
    for quadrant_range in quadrant_ranges:
        quadrant_counter = 0
        height_range, width_range = quadrant_range
        for robot_pos in robot_positions:
            if robot_pos[0] in height_range and robot_pos[1] in width_range:
                quadrant_counter += 1
        res *= quadrant_counter
    return res


def get_next_robot_position(robot_pos, robot_v, h, w):
    y, x = robot_pos
    y_diff, x_diff = robot_v
    y = (y + y_diff) % h
    x = (x + x_diff) % w
    return (y, x)


def find_robot_modulo_positions(robot_pos, robot_v, h, w): # bad part two guess ;)
    original_pos = robot_pos
    res = list()
    while True:
        res.append(robot_pos)
        robot_pos = get_next_robot_position(robot_pos, robot_v, h, w)
        if robot_pos == original_pos:
            break
    return res


def simulate_robots(robots: list[list[list, list]], h, w, iterations: int=100):
    res_positions = list()
    for robot in robots:
        positions = find_robot_modulo_positions(robot[0], robot[1], h, w)
        position_index = iterations % len(positions)
        res_positions.append(positions[position_index])
    return count_robots_in_quadrants(res_positions, h, w)


def check_if_unique(robot_positions):
    unique_positions = set(robot_positions)
    return len(unique_positions) == len(robot_positions)


def find_christmas_tree(robots, h, w):
    counter = 0
    robot_positions = list(map(lambda x: x[0], robots))
    robot_velocities = list(map(lambda x: x[1], robots))
    while not check_if_unique(robot_positions):
        for i in range(len(robot_positions)):
            robot_positions[i] = get_next_robot_position(robot_positions[i], robot_velocities[i], h, w)
        counter += 1
    for i in range(h):
        for j in range(w):
            if (i, j) in robot_positions:
                print('*', end='')
            else:
                print(" ", end="")
        print()
    return counter
    

def solution():
    lines = get_lines('inputs/input14')
    h=103
    w=101
    robots = parse_input(lines)
    print(simulate_robots(robots, h, w))
    print(find_christmas_tree(robots, h, w))

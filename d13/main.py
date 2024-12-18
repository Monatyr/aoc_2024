from utils.utils import *


def parse_input(lines: list):
    token_sets = []
    for line in lines:
        if "A" in line or "B" in line or "Prize" in line:
            diff = line.split(": ")[1]
            x, y = list(map(lambda x: int(x), list(map(lambda x: x[2:], diff.split(", ")))))
        if "A" in line:
            latest = [(x, y)]
        elif "B" in line or "Prize" in line:
            latest.append((x, y))
        if "Prize" in line:
            token_sets.append(latest)
    return token_sets


def check_options(token_set: list[list]):
    a, b = token_set[0]
    c, d = token_set[1]
    X, Y = token_set[2]
    n = (Y - b * X / a) / (d - b * c / a)
    m = (X - n * c) / a
    m = round(m, 3)
    n = round(n, 3)
    if int(m) == m and int(n) == n and m >= 0 and n >= 0:
        return int(3 * m + n)
    return 0


def get_min_tokens(token_sets: list[list]):
    res = 0
    for token_set in token_sets:
        res += check_options(token_set)
    return res


def solution():
    lines = get_lines('inputs/input13')
    token_sets = parse_input(lines)
    print(get_min_tokens(token_sets))

    part_two_addition = int(1e13)
    token_sets_part_two = list(map(lambda x: [x[0], x[1], [x[2][0] + part_two_addition, x[2][1] + part_two_addition]], token_sets))
    print(get_min_tokens(token_sets_part_two))

from utils.utils import *


def find_antennas(lines: list[str]):
    freq_antennas = dict()
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '.':
                continue
            if not freq_antennas.get(c):
                freq_antennas[c] = [(i, j)]
            else:
                freq_antennas[c].append((i, j))
    return freq_antennas


def find_antinodes_positions(pos1, pos2, h, w, part_two):
    diff = (pos2[0] - pos1[0], pos2[1] - pos1[1])
    if not part_two:
        res = [(pos1[0] - diff[0], pos1[1] - diff[1]), (pos2[0] + diff[0], pos2[1] + diff[1])]
    else:
        res = []
        y, x = pos1
        while in_bounds(y, x, h, w):
            res.append((y, x))
            y, x = y - diff[0], x - diff[1]
        y, x = pos2
        while in_bounds(y, x, h, w):
            res.append((y, x))
            y, x = y + diff[0], x + diff[1]
    return list(filter(lambda x: in_bounds(x[0], x[1], h, w), res))
    

def find_antinodes(lines: list[str], part_two=False):
    h, w = len(lines), len(lines[0])
    antinodes = set()
    freq_antennas = find_antennas(lines)
    for v in freq_antennas.values():
        for i in range(len(v) - 1):
            for j in range(i + 1, len(v)):
                antinode_positions = find_antinodes_positions(v[i], v[j], h, w, part_two)
                for pos in antinode_positions:
                    antinodes.add(pos)
    return len(antinodes)


def solution():
    lines = get_lines('inputs/input8')
    print(find_antinodes(lines))
    print(find_antinodes(lines, True))
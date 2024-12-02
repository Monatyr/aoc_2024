from utils.utils import *


def test_report(report: list[int]):
    prev_diff = 0
    for i in range(1, len(report)):
        diff = report[i] - report[i-1]
        if abs(diff) < 1 or abs(diff) > 3 or prev_diff * diff < 0:
            return False
        prev_diff = diff
    return True


def p1(lines: list):
    counter = 0
    for line in lines:
        if test_report(line):
            counter += 1
    return counter

# brute force ;(
def p2(lines: list):
    counter = 0
    for line in lines:
        if test_report(line):
            counter += 1
            continue
        for i in range(len(line)):
            cut_line = line[:i] + line[i+1:]
            if test_report(cut_line):
                counter += 1
                break
    return counter


def solution():
    lines = get_lines('inputs/input2')
    lines = [list(map(lambda x: int(x), el.split())) for el in lines]
    print(p1(lines))
    print(p2(lines))
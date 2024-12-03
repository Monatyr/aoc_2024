from utils.utils import *


def get_result(line, part_two=False, enabled=True):
    res, i = 0, 0
    while i < len(line):
        n1, n2 = 0, 0
        if part_two:
            if line[i:i+4] == "do()":
                enabled = True
                i += 4
                continue
            if line[i:i+7] == "don't()":
                enabled = False
                i += 7
                continue
        if line[i:i+4] != "mul(":
            i += 1
            continue
        i += 4
        j = i
        if line[j] == '0':
            i = j + 1
            continue
        while line[j].isdigit():
            j += 1
        if part_two:
            if line[j:j+4] == "do()":
                enabled = True
                i = j + 4
                continue
            elif line[j:j+7] == "don't()":
                enabled = False
                i = j + 7
                continue
        if line[j] != ',':
            i = j
            continue
        n1 = int(line[i:j])
        j += 1
        i = j
        if line[j] == '0':
            i = j + 1
            continue
        while line[j].isdigit():
            j += 1
        if part_two:
            if line[j:j+4] == "do()":
                enabled = True
                i = j + 4
                continue
            elif line[j:j+7] == "don't()":
                enabled = False
                i = j + 7
                continue
        if line[j] != ')':
            i = j
            continue
        n2 = int(line[i:j])
        if enabled:
            res += n1 * n2
    return (res, None) if not part_two else (res, enabled)


def p1(lines: list):
    res = 0
    for line in lines:
        res += get_result(line)[0]
    return res



def p2(lines: list):
    res, enabled = 0, True
    for line in lines:
        part_res, enabled = get_result(line, True, enabled)
        res += part_res
    return res


def solution():
    lines = get_lines('inputs/input3')
    print(p1(lines))
    print(p2(lines))

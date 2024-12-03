from utils.utils import *
import re


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
    return (res, enabled)


def get_result_regex(line, part_two=False, enabled=True):
    res = 0
    if not part_two:
        regex = r'mul\((?:[1-9][0-9]{0,2}|0),(?:[1-9][0-9]{0,2}|0)\)'
    else:
        regex = r'(?:mul\((?:[1-9][0-9]{0,2}|0),(?:[1-9][0-9]{0,2}|0)\))|do\(\)|don\'t\(\)'
    matches = re.findall(regex, line)
    for match in matches:
        if part_two:
            if match == "do()":
                enabled = True
                continue
            elif match == "don't()":
                enabled = False
                continue
        match = match[4:]
        match = match[:len(match)-1]
        n1, n2 = list(map(lambda x: int(x), match.split(',')))
        if part_two and not enabled:
            continue
        res += n1 * n2
    return res, enabled


def p1(lines: list):
    res1, res2 = 0, 0
    for line in lines:
        res1 += get_result(line)[0]
        res2 += get_result_regex(line)[0]
    print(f"\n--- PART 1 ---\nNormal solution: {res1}\nRegex solution: {res2}")
    return re


def p2(lines: list):
    res1, res2, enabled1, enabled2 = 0, 0, True, True
    for line in lines:
        part_res1, enabled1 = get_result(line, True, enabled1)
        part_res2, enabled2 = get_result_regex(line, True, enabled2)
        res1 += part_res1
        res2 += part_res2
    print(f"\n--- PART 2 ---\nNormal solution: {res1}\nRegex solution: {res2}")


def solution():
    lines = get_lines('inputs/input3')
    p1(lines)
    p2(lines)

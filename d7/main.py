from utils.utils import *


def split_value(value, split_part):
    number_of_digits = len(str(split_part))
    return (value - split_part) / (10 ** number_of_digits)


def can_split(value, split_part):
    split_res = split_value(value, split_part)
    return split_res == int(value / (10 ** len(str(split_part))))


def check_number(value, constituents, part_two=False):
    if len(constituents) == 2:
        if part_two and split_value(value, constituents[1]) == constituents[0]:
            return True
        return value - constituents[1] == constituents[0] or \
               value / constituents[1] == constituents[0]
    division_result = value / constituents[-1]
    if division_result == int(division_result):
        if check_number(division_result, constituents[:len(constituents) - 1], part_two):
            return True
    subtraction_result = value - constituents[-1]
    if subtraction_result > 0:
        if check_number(subtraction_result, constituents[:len(constituents) - 1], part_two):
            return True
    if part_two and can_split(value, constituents[-1]):
        split_result = split_value(value, constituents[-1])
        if check_number(split_result, constituents[:len(constituents) - 1], part_two):
            return True
    return False


def count_valid_operations(lines: list, part_two=False):
    res = 0
    for line in lines:
        value, constituents = line.split(": ")
        value = int(value)
        constituents = list(map(lambda x: int(x), constituents.split(" ")))
        if check_number(value, constituents, part_two):
            res += value
    return res


def solution():
    lines = get_lines('inputs/input7')
    print(count_valid_operations(lines))
    print(count_valid_operations(lines, True))

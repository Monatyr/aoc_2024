from utils.utils import *


rules, orderings = [], []


def check_placement(a, b, rules):
    for rule in rules:
        n1, n2 = list(map(lambda x: int(x), rule.split('|')))
        if b == n1 and a == n2:
            return False
    return True


def check_ordering(ordering, rules):
    for i in range(len(ordering) - 1):
        n1 = ordering[i]
        for j in range(i + 1, len(ordering)):
            n2 = ordering[j]
            if not check_placement(n1, n2, rules):
                return False
    return True


def custom_comparator(a, b):
    global rules
    for rule in rules:
        n1, n2 = list(map(lambda x: int(x), rule.split('|')))
        if b == n1 and a == n2:
            return 1
        if a == n1 and b == n2:
            return -1
    return 0


def sum_middle_values(orderings, rules, part_two=False):
    res = 0
    for ordering in orderings:
        is_correctly_ordered = check_ordering(ordering, rules)
        if is_correctly_ordered and not part_two:
            res += ordering[len(ordering)//2]
        if not is_correctly_ordered and part_two:
            correct_ordering = sort(ordering, custom_comparator)
            res += correct_ordering[len(correct_ordering)//2]
    return res


def solution():
    lines = get_lines('inputs/input5')
    for line in lines:
        if '|' in line:
            rules.append(line)
        elif ',' in line:
            orderings.append(list(map(lambda x: int(x), line.split(','))))
    print(sum_middle_values(orderings, rules))
    print(sum_middle_values(orderings, rules, True))

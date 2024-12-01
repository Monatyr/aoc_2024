from utils.utils import *


def p1(l1: list, l2: list):
    res = 0
    for i in range(len(l1)):
        res += abs(l1[i] - l2[i])
    return res


def p2(l1: list, l2):
    res = 0
    for i in range(len(l1)):
        counter = 0
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                counter += 1
        res += l1[i] * counter
    return res


def solution():
    lines = get_lines('inputs/input1')
    split_lines = list(map(lambda x: x.split(), lines))
    l1, l2 = zip(*split_lines)
    l1 = sort(list(map(lambda x: int(x), l1)))
    l2 = sort(list(map(lambda x: int(x), l2)))
    print(p1(l1, l2))
    print(p2(l1, l2))

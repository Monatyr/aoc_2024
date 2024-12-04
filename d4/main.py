from utils.utils import *


def in_bounds(i, j, h, w):
    return i >= 0 and j >= 0 and i < h and j < w


def check_direction(lines, search_word, x, y, x_diff, y_diff, h, w):
    i, j, word = y, x, ''
    while in_bounds(i, j, h, w) and len(word) < len(search_word):
        word += lines[i][j]
        i += y_diff
        j += x_diff
    if len(word) != len(search_word):
        return 0
    if word == search_word:
        return 1
    return 0


def check_x_mas(lines, search_word, x, y, h, w):
    counter = 0
    for y_diff in (-1, 1):
        for x_diff in (-1, 1):
            if y >= 1 and x >= 1 and y < h - 1 and x < w - 1:
                word = lines[y + y_diff][x + x_diff] + 'A' + lines[y - y_diff][x - x_diff]
                if word == search_word:
                    counter += 1
                elif str(reversed(word)) == search_word:
                    counter += 1
    return counter // 2
    
    
def find_xmas(lines: list[list[str]], part_two):
    search_word = "MAS" if part_two else "XMAS"
    h, w = len(lines), len(lines[0])
    counter = 0
    for i in range(h):
        for j in range(w):
            if not part_two:
                for y_diff in range(-1, 2):
                    for x_diff in range(-1, 2):
                        if y_diff == 0 and x_diff == 0:
                            continue
                        counter += check_direction(lines, search_word, j, i, x_diff, y_diff, h, w)
            elif lines[i][j] == 'A':
                counter += check_x_mas(lines, search_word, j, i, h, w)
    return counter


def solution():
    lines = get_lines('inputs/input4')
    print(find_xmas(lines, False))
    print(find_xmas(lines, True))
    
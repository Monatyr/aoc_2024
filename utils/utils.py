import requests
import sys
import os
from dotenv import load_dotenv

load_dotenv()
AOC_URL = 'https://adventofcode.com/2024/day/'
session_token = os.getenv('AOC_TOKEN')


def get_lines(filename: str):
    with open(filename) as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))
    return lines


def get_input(day: int):
    url = AOC_URL + f'{day}/input'
    headers = {'Cookie': 'session=' + session_token}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return r.content
    else:
        sys.exit(f"response: {r.status_code}: {r.reason} \n{r.content}")


def save_input(day: int):
    if os.path.isfile(f'inputs/input{day}'):
        print('Input file already exists!')
        return
    data = get_input(day).decode()
    with open(f'inputs/input{day}', 'w') as file:
        file.write(data)


def post_solution(day: int, part: int, data):
    url = AOC_URL + f'{day}/{part}'
    headers = {'Cookie': 'session=' + session_token}
    r = requests.post(url, data=data, headers=headers)
    if r.status_code == 200:
        print(r.content)
    else:
        sys.exit(f"response: {r.status_code}: {r.reason} \n{r.content}")


def default_comparator(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    return 0


def sort(lines: list[int], comparator=default_comparator) -> list[int]:
    if len(lines) <= 1:
        return lines
    pivot = lines[0]
    less, eq, more = [], [], []
    for el in lines:
        if comparator(el, pivot) == -1:
            less.append(el)
        elif comparator(el, pivot) == 0:
            eq.append(el)
        else:
            more.append(el)
    return sort(less, comparator) + eq + sort(more, comparator)


def in_bounds(i, j, h, w):
    return i >= 0 and j >= 0 and i < h and j < w
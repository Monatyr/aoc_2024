from utils.utils import *


def evolve_number(number):
    if number == 0:
        return 1, None
    digits = how_many_digits(number)
    if digits % 2 == 0:
        number = str(number)
        n1, n2 = number[:digits//2], number[digits//2:]
        n2 = n2.lstrip('0') or '0'
        return int(n1), int(n2)
    return 2024 * number, None


def blink(numbers: list[int]):
    new_list = []
    for number in numbers:
        n1, n2 = evolve_number(number)
        new_list.append(n1)
        if n2 is not None:
            new_list.append(n2)
    return new_list


def simulate_blinking(numbers: list[int], iterations: int, memoized_results: dict[dict[int, int]]):
    n = len(numbers)
    if iterations == 0:
        return n
    if n == 0:
        return 0
    if n == 1:
        iterations_dict = memoized_results.get(iterations)
        if iterations_dict.get(numbers[0]) is not None:
            return iterations_dict.get(numbers[0])
        res = simulate_blinking(blink(numbers), iterations-1, memoized_results)
        iterations_dict[numbers[0]] = res
    left_part, right_part = numbers[:n//2], numbers[n//2:]
    left_len = simulate_blinking(blink(left_part), iterations-1, memoized_results)
    right_len = simulate_blinking(blink(right_part), iterations-1, memoized_results)
    return left_len + right_len
        

def solution():
    numbers = list(map(lambda x: int(x), get_lines('inputs/input11')[0].split()))
    iterations_dict_25 = {k: dict() for k in range(1, 26)}
    iterations_dict_75 = {k: dict() for k in range(1, 76)}
    print(simulate_blinking(numbers, 25, iterations_dict_25))
    print(simulate_blinking(numbers, 75, iterations_dict_75))
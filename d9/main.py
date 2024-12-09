from utils.utils import *


def data_blocks_checksum(data: list[int]):
    n = len(data)
    i = 0 # id of the data block I'm looking at
    j = n - 1 # id of the first data piece to be moved
    blocks_to_move = data[j] # how many data blocks to move
    block_index = 0 # which data block I'm looking at
    checksum = 0
    while i < j:
        if i % 2 == 0: # if I'm looking at a data sequence
            for _ in range(data[i]):
                checksum += i // 2 * block_index
                block_index += 1
        else: # I'm looking at an empty space in memory
            empty_space_size = data[i]
            while empty_space_size > 0:
                if blocks_to_move == 0:
                    j -= 2
                    blocks_to_move = data[j]
                if i >= j:
                    break
                checksum += j // 2 * block_index
                block_index += 1
                empty_space_size -= 1
                blocks_to_move -= 1
        i += 1
    return checksum


def data_file_checksum(data: list[int]):
    n = len(data)
    i = 0
    j = n - 1
    block_index = 0
    checksum = 0
    moved = set()
    for i in range(n):
        if i % 2 == 0:
            if i in moved:
                block_index += data[i]
                continue
            for _ in range(data[i]):
                checksum += i // 2 * block_index
                block_index += 1
        else:
            for j in range(n-1, i, -2):
                if j in moved:
                    continue
                if data[i] == 0:
                    break
                if data[j] <= data[i]:
                    moved.add(j)
                    for _ in range(data[j]):
                        checksum += j // 2 * block_index
                        block_index += 1
                    data[i] -= data[j]
            block_index += data[i]
    return checksum


def solution():
    data = list(map(lambda x: int(x), get_lines('inputs/input9')[0]))
    print(data_blocks_checksum(data))
    print(data_file_checksum(data))

from utils.utils import *


def get_direction(char):
    if char == "^":
        return (-1, 0)
    if char == "v":
        return (1, 0)
    if char == "<":
        return (0, -1)
    return (0, 1)


def parse_input(lines):
    boxes, walls, moves = set(), set(), list()
    for i, line in enumerate(lines):
        if len(line) == 0:
            h = i
            index = i
            break
        w = len(line)
        for j, el in enumerate(line):
            if el == "@":
                robot_pos = (i, j)
            elif el == "O":
                boxes.add((i, j))
            elif el == "#":
                walls.add((i, j))
    for i in range(index + 1, len(lines)):
        moves.extend(lines[i])
    return robot_pos, boxes, walls, moves, h, w


def expand_map(robot_pos: tuple, boxes: set, walls: set):
    robot_pos = (robot_pos[0], robot_pos[1] * 2)
    new_boxes, new_walls = set(), set()
    for box in boxes:
        new_boxes.add((box[0], (box[1] * 2, box[1] * 2 + 1))) # (box_height, (left_box_edge, right_box_edge))
    for wall in walls:
        new_walls.add((wall[0], wall[1] * 2))
        new_walls.add((wall[0], wall[1] * 2 + 1))
    return robot_pos, new_boxes, new_walls


def simulate_robot_move(robot_pos: tuple, boxes: set, walls: set, move_direction: tuple):
    new_robot_pos = (robot_pos[0] + move_direction[0], robot_pos[1] + move_direction[1])
    if new_robot_pos in walls:
        return robot_pos
    if new_robot_pos in boxes:
        current_position = new_robot_pos
        while current_position in boxes:
            current_position = (current_position[0] + move_direction[0], current_position[1] + move_direction[1])
            if current_position in walls:
                return robot_pos
        boxes.remove(new_robot_pos)
        boxes.add(current_position)
        return new_robot_pos
    return new_robot_pos


def check_box_collision(pos: tuple, original_pos: tuple, boxes: set): # return box if positions collide
    if not isinstance(pos[1], tuple): # robot
        for box in boxes:
            if pos[0] == box[0] and (pos[1] == box[1][0] or pos[1] == box[1][1]):
                return { box }
    else: # box
        res = set()
        for box in boxes:
            if box == original_pos:
                continue
            if pos[0] == box[0] and (pos[1][0] == box[1][0] or pos[1][0] == box[1][1] or pos[1][1] == box[1][0]):
                res.add(box)
        return res
    return None


def recursive_check_if_can_move(pos: tuple, boxes: set, walls: set, move_direction: tuple, resulting_boxes: set):
    if not isinstance(pos[1], tuple):
        target_pos = (pos[0] + move_direction[0], pos[1] + move_direction[1])
        if target_pos in walls:
            return False
    else:
        resulting_boxes.add(pos)
        target_pos = (pos[0] + move_direction[0], (pos[1][0] + move_direction[1], pos[1][1] + move_direction[1]))
        if (target_pos[0], target_pos[1][0]) in walls or (target_pos[0], target_pos[1][1]) in walls:
            return False
    colliding_boxes = check_box_collision(target_pos, pos, boxes)
    if colliding_boxes is None:
        return True
    for box in colliding_boxes:
        if not recursive_check_if_can_move(box, boxes, walls, move_direction, resulting_boxes):
            return False
    return True


def simulate_robot_move_part_two(robot_pos: tuple, boxes: set, walls: set, move_direction: tuple):
    new_robot_pos = (robot_pos[0] + move_direction[0], robot_pos[1] + move_direction[1])
    if new_robot_pos in walls:
        return robot_pos
    resulting_boxes = set()
    if not recursive_check_if_can_move(robot_pos, boxes, walls, move_direction, resulting_boxes):
        return robot_pos
    for box in resulting_boxes:
        boxes.remove(box)
    for box in resulting_boxes:
        boxes.add((box[0] + move_direction[0], (box[1][0] + move_direction[1], box[1][1] + move_direction[1])))
    return new_robot_pos


def simulate_moves(robot_pos: tuple, boxes: set, walls: set, moves: list, part_two: bool=False):
    res = 0
    for i, move in enumerate(moves):
        direction_tuple = get_direction(move)
        if not part_two:
            robot_pos = simulate_robot_move(robot_pos, boxes, walls, direction_tuple)
        else:
            robot_pos = simulate_robot_move_part_two(robot_pos, boxes, walls, direction_tuple)
    for box in boxes:
        if not part_two:
            res += box[0] * 100 + box[1]
        else:
            res += box[0] * 100 + box[1][0]
    return res


def solution():
    lines = get_lines('inputs/input15')
    # p1
    robot_pos, boxes, walls, moves, h, w = parse_input(lines)
    print(simulate_moves(robot_pos, boxes, walls, moves))
    # p2
    robot_pos, boxes, walls, moves, h, w = parse_input(lines)
    robot_pos, boxes, walls = expand_map(robot_pos, boxes, walls)
    print(simulate_moves(robot_pos, boxes, walls, moves, True))

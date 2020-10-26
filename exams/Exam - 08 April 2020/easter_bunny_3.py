import sys

def create_field(size):
    return [input().split(" ") for _ in range(size)]


def are_valid_indexes(i, j, matrix):
    return i in range(len(matrix)) and j in range(len(matrix))


def find_bunny(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == "B":
                return i, j


def move_and_count_eggs(dr, dc, matrix):
    bunny_row, bunny_col = find_bunny(matrix)
    row, col = bunny_row + dr, bunny_col + dc
    count = 0
    pos = []

    while are_valid_indexes(row, col, matrix):
        if matrix[row][col] == "X":
            break
        else:
            count += int(matrix[row][col])
            pos.append([row, col])
            row += dr
            col += dc

    return count, pos


def easter_bunny(matrix):
    directions = {
        "up": lambda: move_and_count_eggs(-1, 0, matrix),
        "down": lambda: move_and_count_eggs(1, 0, matrix),
        "left": lambda: move_and_count_eggs(0, -1, matrix),
        "right": lambda: move_and_count_eggs(0, 1, matrix),
    }
    max_eggs = -sys.maxsize
    max_pos = []
    max_direction = ""

    for d in directions:
        fn = directions[d]
        count, pos = fn()
        if count >= max_eggs:
            max_eggs = count
            max_pos = pos
            max_direction = d

    return max_direction, max_pos, max_eggs,


field_size = int(input())
field = create_field(field_size)
direction, positions, eggs = easter_bunny(field)
print(direction)
[print(pos) for pos in positions]
print(eggs)

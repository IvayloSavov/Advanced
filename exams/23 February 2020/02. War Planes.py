def find_plane(matrix):
    targets = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == "p":
                plane_pos = i, j
            elif matrix[i][j] == "t":
                targets += 1

    return plane_pos, targets


def new_directions(c_row, c_col, steps):
    return int(c_row) * int(steps), int(c_col) * int(steps)


def is_valid_indexes(matrix, row, col):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix)


def war_planes(matrix, cmd, way, step):
    global all_targets
    directions = {
        "right": (0, 1),
        "left": (0, -1),
        "up": (-1, 0),
        "down": (1, 0),
    }
    win_game = False
    current_direction_row, current_direction_col = directions[way]
    c_row_step, c_col_step = new_directions(current_direction_row, current_direction_col, step)
    plane_row, plane_col = find_plane(matrix)[0]

    row, col = plane_row + c_row_step, plane_col + c_col_step

    if is_valid_indexes(matrix, row, col):
        if cmd == "move":
            if matrix[row][col] == ".":
                matrix[plane_row][plane_col] = "."
                matrix[row][col] = "p"
        elif cmd == "shoot":
            if matrix[row][col] == "t":
                all_targets -= 1
            matrix[row][col] = "x"

            if all_targets == 0:
                win_game = True
                return win_game


size_of_field = int(input())

field = [input().split() for _ in range(size_of_field)]
all_targets = find_plane(field)[1]
all_targets_copy = all_targets

for _ in range(int(input())):
    command, direction, steps = input().split()
    res = war_planes(field, command, direction, steps)
    if res:
        break

if res:
    print(f"Mission accomplished! All {all_targets_copy} targets destroyed.")
else:
    print(f"Mission failed! {all_targets} targets left.")

[print(*row) for row in field]
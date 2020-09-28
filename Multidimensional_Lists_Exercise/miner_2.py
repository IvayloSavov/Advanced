from collections import deque


def index_validate(matrix_length, number):
    if -1 < number < matrix_length:
        return True
    return False


current_position = None
coal_count = 0

size = int(input())
commands = deque(input().split())

matrix = []
for r in range(size):
    row = input().split()
    if 's' in row:
        current_position = r, row.index('s')

    if 'c' in row:
        coal_count += row.count('c')

    matrix.append(row)

commands_over = False
while not commands_over:
    if not commands:
        commands_over = True
        break

    command = commands.popleft()
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

    row_add, column_add = directions[command]
    cur_row, cur_column = current_position
    new_row, new_column = cur_row + row_add, cur_column + column_add

    if not index_validate(len(matrix), new_row) or \
            not index_validate(len(matrix), new_column):
        continue

    current_position = new_row, new_column
    matrix[cur_row][cur_column] = "*"
    new_elem = matrix[new_row][new_column]

    if new_elem == "c":
        coal_count -= 1
        matrix[new_row][new_column] = "*"

        if coal_count == 0:
            print(f"You collected all coals! {new_row, new_column}")
            break

    elif new_elem == "e":
        print(f"Game over! {new_row, new_column}")
        break

if commands_over:
    new_row, new_column = current_position
    print(f"{coal_count} coals left. {new_row, new_column}")
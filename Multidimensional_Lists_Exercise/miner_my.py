from collections import deque


def count_all_coals(matrix):
    coals = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == "c":
                coals += 1
    return coals


def find_miner(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == "s":
                return i, j


def is_valid_index(index):
    return 0 <= index < size_of_field


def moving_miner(matrix, command):
    miner_row, miner_col = find_miner(matrix)
    if command == "up":
        if is_valid_index(miner_row - 1):
            if matrix[miner_row - 1][miner_col] == "e":
                return miner_row - 1, miner_col
            matrix[miner_row][miner_col] = "*"
            matrix[miner_row - 1][miner_col] = "s"

    elif command == "down":
        if is_valid_index(miner_row + 1):
            if matrix[miner_row + 1][miner_col] == "e":
                return miner_row + 1, miner_col
            matrix[miner_row][miner_col] = "*"
            matrix[miner_row + 1][miner_col] = "s"

    elif command == "left":
        if is_valid_index(miner_col - 1):
            if matrix[miner_row][miner_col - 1] == "e":
                return miner_row, miner_col - 1
            matrix[miner_row][miner_col] = "*"
            matrix[miner_row][miner_col - 1] = "s"

    elif command == "right":
        if is_valid_index(miner_col + 1):
            if matrix[miner_row][miner_col + 1] == "e":
                return miner_row, miner_col + 1
            matrix[miner_row][miner_col] = "*"
            matrix[miner_row][miner_col + 1] = "s"


size_of_field = int(input())
commands = deque(input().split(" "))

field = [input().split(" ") for _ in range(size_of_field)]
is_game_over = False
found_all_coals = False

while commands:
    if count_all_coals(field) == 0:
        found_all_coals = True
        break
    current_command = commands.popleft()
    res = moving_miner(field, current_command)
    if res is not None:
        print(f"Game over! {res}")
        is_game_over = True
        break

if count_all_coals(field) == 0 and not is_game_over:
    found_all_coals = True
    row_index, col_index = find_miner(field)
    print(f"You collected all coals! ({row_index}, {col_index})")

if not is_game_over and not found_all_coals:
    row_index, col_index = find_miner(field)
    print(f"{count_all_coals(field)} coals left. ({row_index}, {col_index})")

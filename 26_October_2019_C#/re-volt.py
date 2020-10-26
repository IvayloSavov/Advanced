def find_player(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == "f":
                return i, j


def are_valid_indexes(row, col, matrix):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix)


def check_which_one_is_invalid(row, col, matrix):
    if row > len(matrix) - 1:
        row = 0
    elif row < 0:
        row = len(matrix) - 1

    elif col > len(matrix) - 1:
        col = 0
    elif col < 0:
        col = len(matrix) - 1

    return row, col


def re_volt(matrix, count_cmd):
    is_win = False
    directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
    for _ in range(count_cmd):
        command = input()
        cmd_row, cmd_col = directions[command]
        p_row, p_col = find_player(matrix)
        new_row, new_col = p_row + cmd_row, p_col + cmd_col

        matrix[p_row][p_col] = "-"
        if not are_valid_indexes(new_row, new_col, matrix):
            new_row, new_col = check_which_one_is_invalid(new_row, new_col, matrix)

        if matrix[new_row][new_col] == "F":
            is_win = True
        elif matrix[new_row][new_col] == "B":
            new_row, new_col = new_row + cmd_row, new_col + cmd_col
            if not are_valid_indexes(new_row, new_col, matrix):
                new_row, new_col = check_which_one_is_invalid(new_row, new_col, matrix)
            if matrix[new_row][new_col] == "F":
                is_win = True

        elif matrix[new_row][new_col] == "T":
            new_row, new_col = new_row - cmd_row, new_col - cmd_col
            if not are_valid_indexes(new_row, new_col, matrix):
                new_row, new_col = check_which_one_is_invalid(new_row, new_col, matrix)
        matrix[new_row][new_col] = "f"
        if is_win:
            break
    return is_win


size = int(input())
count_commands = int(input())

field = [[*input()] for _ in range(size)]
res = re_volt(field, count_commands)
print("Player won!") if res else print("Player lost!")
[print("".join(row)) for row in field]
def find_worm(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == "P":
                return i, j


def are_valid_indexes(row_index, col_index, matrix):
    return 0 <= row_index < len(matrix) and 0 <= col_index < len(matrix)


def print_matrix_and_string(matrix, text):
    print(text)
    [print("".join(row)) for row in matrix]


def snake(matrix, text):
    directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1),}
    for _ in range(int(input())):
        command = input()
        cmd_row, cmd_col = directions[command]
        worm_row, worm_col = find_worm(matrix)
        new_row, new_col = cmd_row + worm_row, cmd_col + worm_col

        if are_valid_indexes(new_row, new_col, matrix):
            matrix[worm_row][worm_col] = "-"
            if matrix[new_row][new_col].isalpha():
                text += matrix[new_row][new_col]
            matrix[new_row][new_col] = "P"
        else:
            text = text[:-1]
    return text


string = input()
size = int(input())

field = [[*input()] for _ in range(size)]
string = snake(field, string)
print_matrix_and_string(field, string)

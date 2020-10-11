import re


def is_valid_index(index, matrix):
    return 0 <= index < len(matrix)


def placing_bombs(matrix, count_bombs):
    while count_bombs:
        command = input()
        positions = re.findall(r"\d+", command)
        row = int(positions[0])
        col = int(positions[1])
        if is_valid_index(row, matrix) and is_valid_index(col, matrix):
            matrix[row][col] = "*"
            count_bombs -= 1


def counting_bombs_around_pos(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] != "*":
                counter_bombs = 0
                for i in range(row - 1, row + 2):
                    for j in range(col - 1, col + 2):
                        if is_valid_index(i, matrix) and is_valid_index(j, matrix):
                            if matrix[i][j] == "*":
                                counter_bombs += 1
                matrix[row][col] = counter_bombs


size_field = int(input())
number_bombs = int(input())

field = [[" " for _ in range(size_field)] for _ in range(size_field)]
placing_bombs(field, number_bombs)
counting_bombs_around_pos(field)
[print(*row) for row in field]

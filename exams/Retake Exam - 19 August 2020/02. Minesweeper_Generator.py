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


# def are_valid_indexes(matrix, row, col):
#     return row in range(len(matrix)) and col in range(len(matrix))
#
#
# def placing_bombs(matrix, count_b):
#     while count_b > 0:
#         row, col = map(int, (input().strip("()").split(", ")))
#         if are_valid_indexes(matrix, row, col):
#             matrix[row][col] = "*"
#             count_b -= 1
#
#
# def counting_bombs_around_pos(row, col, matrix):
#     pos_count_bombs = 0
#     for k in range(row - 1, row + 2):
#         for m in range(col - 1, col + 2):
#             if are_valid_indexes(matrix, k, m) and matrix[k][m] == "*":
#                 pos_count_bombs += 1
#     return pos_count_bombs
#
#
# field_size = int(input())
# count_bombs = int(input())
# field = [[0] * field_size for _ in range(field_size)]
#
# placing_bombs(field, count_bombs)
#
# for i in range(field_size):
#     for j in range(field_size):
#         if field[i][j] == 0:
#             field[i][j] = counting_bombs_around_pos(i, j, field)
#
# [print(*row) for row in field]
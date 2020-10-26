def find_king(matrix, symbol="K"):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == symbol:
                return i, j


def are_valid_indexes(row, col, matrix):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix)


def get_killer_queens(matrix):
    row_k, col_k = find_king(matrix)
    queens = []
    directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1), "upleft": (-1, -1),
                  "upright": (-1, 1), "downleft": (1, -1), "downright": (1, 1)}
    for row_cmd, col_cmd in directions.values():
        new_row, new_col = row_k + row_cmd, col_k + col_cmd
        while are_valid_indexes(new_row, new_col, matrix):
            if matrix[new_row][new_col] == "Q":
                queens.append([new_row, new_col])
                break
            new_row, new_col = new_row + row_cmd, new_col + col_cmd
    return queens


field = [input().split() for _ in range(8)]
queens = get_killer_queens(field)
if queens:
    [print(queen) for queen in queens]
else:
    print("The king is safe!")

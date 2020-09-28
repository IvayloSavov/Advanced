from collections import deque


def is_valid_index(index, size):
    return 0 <= index <= size


rows, cols = map(int, input().split())
matrix = [input().split() for i in range(rows)]

while True:
    tokens = deque(input().split())
    if tokens[0] == "END":
        break

    if tokens[0] == "swap" and len(tokens) == 5:
        tokens.popleft()
        tokens = map(int, tokens)
        row_1, col_1, row_2, col_2 = tokens
        if is_valid_index(row_1, rows) and is_valid_index(row_2, rows) and is_valid_index(col_1, cols) and \
                is_valid_index(col_2, cols):
            matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
            for row in matrix:
                print(" ".join(map(str, row)))
        else:
            print("Invalid input!")

    else:
        print("Invalid input!")
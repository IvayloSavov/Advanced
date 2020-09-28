from collections import deque
from itertools import chain


def is_valid_index(index, size_matrix):
    return 0 <= index < size_matrix


def exploding_bomb(b_row, b_col, field):
    # Coordinates of the integers around the bomb
    rows = [-1, -1, -1, 0, 0, 1, 1, 1]
    cols = [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(len(rows)):
        current_element_row = b_row + rows[i]
        current_element_col = b_col + cols[i]
        if is_valid_index(current_element_row, len(field)) and is_valid_index(current_element_col, len(field)) \
                and field[current_element_row][current_element_col] > 0:
            bomb_value = field[b_row][b_col]
            field[current_element_row][current_element_col] -= bomb_value


size_of_matrix = int(input())

# Creating the matrix
matrix = [[int(n) for n in input().split()] for _ in range(size_of_matrix)]

# Bombs coordinates
bombs = deque(input().split(" "))

while bombs:
    bombs_coordinates = deque(map(int, bombs.popleft().split(",")))
    bomb_row = bombs_coordinates.popleft()
    bomb_col = bombs_coordinates.popleft()
    if matrix[bomb_row][bomb_col] <= 0:
        continue
    exploding_bomb(bomb_row, bomb_col, matrix)
    matrix[bomb_row][bomb_col] = 0

alive_cells = [e for e in chain(*matrix) if e > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

for row in matrix:
    print(" ".join(list(map(str, row))))


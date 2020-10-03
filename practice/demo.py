from sys import maxsize
from collections import deque


def find_bunny(matrix):
    for m in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[m][j] == "B":
                return m, j


def counting_eggs(matrix, direction):
    current_sum_eggs = 0
    current_eggs_position = []
    row_bunny, col_bunny = find_bunny(matrix)
    global max_eggs
    global max_eggs_positions
    global max_direction

    if direction == "up":
        for i in range(row_bunny - 1, -1, -1):
            if not 0 <= i < len(matrix) or matrix[i][col_bunny] == "X":
                break
            current_sum_eggs += int(matrix[i][col_bunny])
            current_eggs_position.append([i, col_bunny])

    elif direction == "down":
        for i in range(row_bunny + 1, len(matrix)):
            if not 0 <= i < len(matrix) or matrix[i][col_bunny] == "X":
                break
            current_sum_eggs += int(matrix[i][col_bunny])
            current_eggs_position.append([i, col_bunny])

    elif direction == "left":
        for i in range(col_bunny - 1, -1, -1):
            if not 0 <= i < len(matrix) or matrix[row_bunny][i] == "X":
                break
            current_sum_eggs += int(matrix[row_bunny][i])
            current_eggs_position.append([row_bunny, i])

    elif direction == "right":
        for i in range(col_bunny + 1, len(matrix)):
            if not 0 <= i < len(matrix) or matrix[row_bunny][i] == "X":
                break
            current_sum_eggs += int(matrix[row_bunny][i])
            current_eggs_position.append([row_bunny, i])

    if current_sum_eggs >= max_eggs:
        max_eggs = current_sum_eggs
        max_eggs_positions = current_eggs_position
        max_direction = direction


size_field = int(input())
field = []
directions = deque(["up", "down", "left", "right"])
max_eggs = -maxsize
max_eggs_positions = []
max_direction = []

for _ in range(size_field):
    line = input().split(" ")
    field.append(line)

while directions:
    current_direction = directions.popleft()
    counting_eggs(field, current_direction)

print(max_direction)

for row in max_eggs_positions:
    print(row)

print(max_eggs)
from collections import deque

rows, cols = map(int, input().split())
snake = deque(input())

path = [[""] * cols for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        piece_of_snake = snake.popleft()
        if i % 2 == 0:
            path[i][j] = piece_of_snake
        else:
            path[i][cols - 1 - j] = piece_of_snake
        snake.append(piece_of_snake)

for row in path:
    print("".join(row))

# from collections import deque
#
# rows, cols = [int(x) for x in input().split()]
# text = deque(input())
#
# matrix = []
#
# for row in range(rows):
#     matrix.append([])
#     for col in range(cols):
#         matrix[row].append("")
#
# for row in range(rows):
#     for col in range(cols):
#         current_col = col
#         current_char = text.popleft()
#         if row % 2 != 0:
#             current_col = cols - 1 - col # <-
#         matrix[row][current_col] = current_char
#         text.append(current_char)
#
# for row in matrix:
#     print("".join(row))

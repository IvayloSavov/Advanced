from collections import deque

rows, cols = map(int, input().split())
snake = deque(input())

path = [[""] * cols for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        piece_of_snake = snake.popleft()
        path[i][j] = piece_of_snake
        snake.append(piece_of_snake)
    if i % 2 != 0:
        path[i].reverse()

for row in path:
    print("".join(row))
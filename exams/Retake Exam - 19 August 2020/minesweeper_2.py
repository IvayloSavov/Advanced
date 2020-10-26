def bomb_counter(row, col, n):
    bombs_around = 0
    variants = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for combo in variants:
        vertically, horizontally = combo
        if vertically + row in range(n) and horizontally + col in range(n):
            if field[vertically + row][horizontally + col] == "*":
                bombs_around += 1
    return bombs_around


n = int(input())
field = [[0] * n for _ in range(n)]
bombs = int(input())

for bomb in range(bombs):
    row, col = [int(x) for x in input()[1:-1].split(", ")]
    field[row][col] = "*"

for i in range(n):
    for j in range(n):
        if field[i][j] != "*":
            field[i][j] = bomb_counter(i, j, n)

for r in field:
    print(" ".join([str(x) for x in r]))
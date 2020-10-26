size = int(input())
snake_position = []
teleport = []
matrix = []

food_count = 0
dirs = {
    "up": [-1, 0], "right": [0, 1], "down": [1, 0], "left": [0, -1]
}
for i in range(size):
    row = list(input())
    matrix.append(row)
    if "S" in row:
        snake_position = [i, row.index("S")]
    if "B" in row:
        teleport = [i, row.index("B")]
command = input()
while True:
    direction_change = dirs[command]
    next_row = snake_position[0] + direction_change[0]
    next_col = snake_position[1] + direction_change[1]
    next_pos = [next_row, next_col]
    if 0 <= next_row < size and 0 <= next_col < size:
        if matrix[next_row][next_col] == "-":
            matrix[snake_position[0]][snake_position[1]] = "."
            snake_position = next_pos

            matrix[snake_position[0]][snake_position[1]] = "S"

        elif matrix[next_row][next_col] == "B":
            matrix[next_row][next_col] = "."
            matrix[snake_position[0]][snake_position[1]] = "."
            snake_position = teleport
            matrix[snake_position[0]][snake_position[1]] = "S"
        elif matrix[next_row][next_col] == "*":
            food_count += 1
            matrix[snake_position[0]][snake_position[1]] = "."
            snake_position = next_pos
            matrix[snake_position[0]][snake_position[1]] = "S"
        else:
            matrix[snake_position[0]][snake_position[1]] = "-"
            player_pos = next_pos
            matrix[snake_position[0]][snake_position[1]] = "S"

        if food_count == 10:
            print("You won! You fed the snake.")
            print(f"Food eaten: {food_count}")
            [print("".join(row)) for row in matrix]
            break
    else:
        matrix[snake_position[0]][snake_position[1]] = "."
        print("Game over!")
        print(f"Food eaten: {food_count}")
        [print("".join(row)) for row in matrix]
        break
    command = input()
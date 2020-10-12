QUANTITY_FOOD_NEEDED = 10


def are_valid_indexes(row, col, matrix):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix)


def moving_snake(matrix, position_snake):
    food_collected = 0
    game_over = False
    commands = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1),
    }
    while True:
        command = input()
        row_command, col_command = commands[command]
        row_snake, col_snake = position_snake
        move_row, move_col = (row_command + row_snake, col_command + col_snake)
        matrix[row_snake][col_snake] = "."

        if are_valid_indexes(move_row, move_col, matrix):
            if matrix[move_row][move_col] == "*":
                food_collected += 1
            elif matrix[move_row][move_col] == "B":
                matrix[move_row][move_col] = "."
                move_row, move_col = find_snake_boundary(matrix, "B")
            matrix[move_row][move_col] = "S"
            position_snake = move_row, move_col

        else:
            return game_over, food_collected

        if food_collected >= QUANTITY_FOOD_NEEDED:
            game_over = True
            return game_over, food_collected


def find_snake_boundary(matrix, symbol):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == symbol:
                return row, col


territory_size = int(input())
territory = [[ch for ch in input()] for _ in range(territory_size)]
snake_pos = find_snake_boundary(territory, "S")
res, food_eaten = moving_snake(territory, snake_pos)

if res:
    print("You won! You fed the snake.")
else:
    print("Game over!")

print(f"Food eaten: {food_eaten}")
[print(''.join(row)) for row in territory]

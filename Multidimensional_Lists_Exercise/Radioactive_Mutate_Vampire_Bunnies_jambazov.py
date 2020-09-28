def index_validate(matrix_length, number):
    """
    Validates if an index is out of the range of the matrix
    """

    if 0 <= number < matrix_length:
        return True
    return False


row_count, column_count = [int(x) for x in input().split()]

current_position = None
matrix = []
for r in range(row_count):
    row = list(input())
    matrix.append(row)

    if "P" in row:
        c = row.index("P")
        current_position = r, c
        matrix[r][c] = "."

commands = list(input())

game_finished = False
escaped = False
died = False

while not game_finished:
    command = commands.pop(0)

    directions = {
        "U": (-1, 0),
        "D": (1, 0),
        "L": (0, -1),
        "R": (0, 1)
    }

    cur_row, cur_column = current_position
    new_row, new_column = cur_row + directions[command][0], cur_column + directions[command][1]

    current_position = new_row, new_column
    if not index_validate(row_count, new_row) or not index_validate(column_count, new_column):
        game_finished = True
        escaped = True
        current_position = cur_row, cur_column
    else:
        if matrix[new_row][new_column] == "B":
            died = True
            game_finished = True

    recently_added = []
    for r in range(row_count):
        for c in range(column_count):
            if matrix[r][c] != "B" or (r, c) in recently_added:
                continue

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for direction in directions:
                new_r, new_c = r + direction[0], c + direction[1]

                if not index_validate(row_count, new_r) or not index_validate(column_count, new_c):
                    continue

                if matrix[new_r][new_c] == "B":
                    continue

                if (new_r, new_c) == current_position and not escaped:
                    died = True
                    game_finished = True

                matrix[new_r][new_c] = "B"
                recently_added.append((new_r, new_c))


for r in matrix:
    print(''.join([str(x) for x in r]))

cur_row, cur_column = current_position
if escaped:
    print(f"won: {cur_row} {cur_column}")
else:
    print(f"dead: {cur_row} {cur_column}")


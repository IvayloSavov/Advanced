def find_players(matrix):
    first_player = ()
    second_player = ()
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == "f":
                first_player = i, j
            elif matrix[i][j] == "s":
                second_player = i, j
    return first_player, second_player


def new_index_is_in_range_field(index, matrix):
    return 0 <= index < len(matrix)


def print_final_matrix(matrix):
    return [print(''.join(row)) for row in matrix]


def tron_racers(matrix):
    first_pos, second_pos = find_players(matrix)
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1),
    }
    while True:
        first_player_cmd, second_player_cmd = input().split()

        first_row_cmd, first_col_cmd = directions[first_player_cmd]
        second_row_cmd, second_col_cmd = directions[second_player_cmd]

        first_row_pos, first_col_pos = first_pos
        second_row_pos, second_col_pos = second_pos

        new_first_row, new_first_col = first_row_pos + first_row_cmd, first_col_pos + first_col_cmd
        new_second_row, new_second_col = second_row_pos + second_row_cmd, second_col_pos + second_col_cmd

        # Checking the first player
        if new_index_is_in_range_field(new_first_row, matrix) and not new_index_is_in_range_field(new_first_col, matrix):
            if new_first_col < 0:
                new_first_col = len(matrix) - 1
            elif new_first_col > len(matrix) - 1:
                new_first_col = 0

        elif not new_index_is_in_range_field(new_first_row, matrix) and new_index_is_in_range_field(new_first_col, matrix):
            if new_first_row < 0:
                new_first_row = len(matrix) - 1
            elif new_first_row > len(matrix) - 1:
                new_first_row = 0

        if not matrix[new_first_row][new_first_col] == "s":
            matrix[new_first_row][new_first_col] = "f"
        else:
            matrix[new_first_row][new_first_col] = "x"
            break

        # Checking the second player
        if new_index_is_in_range_field(new_second_row, matrix) and not new_index_is_in_range_field(new_second_col, matrix):
            if new_second_col < 0:
                new_second_col = len(matrix) - 1
            elif new_second_col > len(matrix) - 1:
                new_second_col = 0

        elif not new_index_is_in_range_field(new_second_row, matrix) and new_index_is_in_range_field(new_second_col, matrix):
            if new_second_row < 0:
                new_second_row = len(matrix) - 1
            elif new_second_row > len(matrix) - 1:
                new_second_row = 0

        if not matrix[new_second_row][new_second_col] == "f":
            matrix[new_second_row][new_second_col] = "s"
        else:
            matrix[new_second_row][new_second_col] = "x"
            break

        first_pos = (new_first_row, new_first_col)
        second_pos = (new_second_row, new_second_col)

    print_final_matrix(matrix)


size = int(input())
field = [[*input()] for _ in range(size)]
tron_racers(field)

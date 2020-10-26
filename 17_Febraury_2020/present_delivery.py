def find_santa(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == "S":
                return i, j


def count_nice_kids(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == "V":
                count += 1
    return count


def are_valid_indexes(row, col, matrix):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix)


def happy_santa(matrix, row, col):
    not_enough_presents = False
    global count_presents
    directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
    for direction in directions:
        cmd_row, cmd_col = directions[direction]
        new_row, new_col = cmd_row + row, cmd_col + col
        if are_valid_indexes(new_row, new_col, matrix):
            if matrix[new_row][new_col] in "VX":
                if count_presents:
                    count_presents -= 1
                    matrix[new_row][new_col] = "-"
                else:
                    not_enough_presents = True
                    return not_enough_presents
    return not_enough_presents


def present_delivery(matrix):
    global count_presents
    directions = {"left": (0, -1), "right": (0, 1), "up": (-1, 0), "down": (1, 0), }

    command = input()
    while command != "Christmas morning" and count_nice_kids(neighborhood):
        cmd_row, cmd_col = directions[command]
        santa_row, santa_col = find_santa(matrix)
        new_row, new_col = cmd_row + santa_row, cmd_col + santa_col

        if are_valid_indexes(new_row, new_col, matrix):
            matrix[santa_row][santa_col] = "-"
            if matrix[new_row][new_col] == "C":
                is_fail = happy_santa(matrix, new_row, new_col)
                if is_fail:
                    return
            elif matrix[new_row][new_col] == "V":
                count_presents -= 1
            matrix[new_row][new_col] = "S"

        if count_presents <= 0:
            return

        command = input()


count_presents = int(input())
size_field = int(input())

neighborhood = [input().split() for _ in range(size_field)]
nice_kids_begging = count_nice_kids(neighborhood)
present_delivery(neighborhood)
nice_kids_end = count_nice_kids(neighborhood)

if count_presents <= 0 and nice_kids_end:
    print("Santa ran out of presents!")

[print(*row) for row in neighborhood]

if nice_kids_end:
    print(f"No presents for {nice_kids_end} nice kid/s.")
else:
    print(f"Good job, Santa! {nice_kids_begging} happy nice kid/s.")
def count_nice_kids():
    nice_kids = 0
    for i in range(size_neighborhood):
        for j in range(size_neighborhood):
            if neighborhood[i][j] == "V":
                nice_kids += 1
    return nice_kids


def is_valid_index(index, matrix):
    return 0 <= index < len(matrix)


def find_santa():
    for i in range(size_neighborhood):
        for j in range(size_neighborhood):
            if neighborhood[i][j] == "S":
                return i, j


def santa_is_happy(directions_dict, matrix, cookie_row, cookie_col):
    global count_presents
    global nice_children
    no_enough_present = False

    for __direction, values in directions_dict.items():
        __current_row, __current_col = (cookie_row + int(values[0]), cookie_col + int(values[1]))

        if count_presents == 0:
            no_enough_present = True
            break

        if is_valid_index(__current_row, matrix) and is_valid_index(__current_col, matrix):
            if matrix[__current_row][__current_col] == "V" or matrix[__current_row][__current_col] == "X":
                count_presents -= 1
                if matrix[__current_row][__current_col] == "V":
                    nice_children -= 1
                matrix[__current_row][__current_col] = "-"

    return no_enough_present


def present_delivery(matrix, __direction):
    global santa
    global count_presents
    global nice_children
    row, col = directions[__direction]
    santa_row, santa_col = santa

    current_row, current_col = (row + santa_row, col + santa_col)

    if is_valid_index(current_row, matrix) and is_valid_index(current_col, matrix):
        matrix[santa_row][santa_col] = "-"

        if matrix[current_row][current_col] == "V":
            count_presents -= 1
            nice_children -= 1

        elif matrix[current_row][current_col] == "C":
            res = santa_is_happy(directions, matrix, current_row, current_col)
            matrix[current_row][current_col] = "S"
            if res:
                return True

        matrix[current_row][current_col] = "S"
        santa = (current_row, current_col)


count_presents = int(input())
size_neighborhood = int(input())
directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0),
}

neighborhood = [input().split() for _ in range(size_neighborhood)]

nice_children = count_nice_kids()
nice_children_copy = nice_children
santa = find_santa()


while True:
    line = input()
    if line == "Christmas morning":
        break
    direction = line
    result = present_delivery(neighborhood, direction)

    if result is True:
        break

    if count_presents == 0:
        break

# line = input()
# while line != "Christmas morning":
#     direction = line
#     result = present_delivery(neighborhood, direction)
#     if result:
#         break
#
#     if count_presents == 0:
#         break
#
#     line = input()


if count_presents == 0 and nice_children > 0:
    print("Santa ran out of presents!")

[print(" ".join(row)) for row in neighborhood]

if nice_children == 0:
    print(f"Good job, Santa! {nice_children_copy} happy nice kid/s.")
else:
    print(f"No presents for {nice_children} nice kid/s.")
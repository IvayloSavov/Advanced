def find_bunny(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "B":
                return row, col


def easter_bunny(matrix):
    bunny_row, bunny_col = find_bunny(matrix)
    max_pos = ""
    max_field_pos = []
    max_eggs = -999999999999
    directions = ["right", "up", "down", "left"]

    for d in directions:
        current_pos = []
        is_valid_index = True
        if d == "right":
            if 0 <= bunny_col + 1 < len(matrix[bunny_row]):
                current_eggs = 0
                for c_col in range(bunny_col + 1, len(matrix[bunny_row])):
                    if matrix[bunny_row][c_col] == "X":
                        break
                    current_eggs += int(matrix[bunny_row][c_col])
                    current_pos.append([bunny_row, c_col])
            else:
                is_valid_index = False

        elif d == "up":
            if 0 <= bunny_row - 1 < len(matrix):
                current_eggs = 0
                for c_row in range(bunny_row - 1, -1, -1):
                    if matrix[c_row][bunny_col] == "X":
                        break
                    current_eggs += int(matrix[c_row][bunny_col])
                    current_pos.append([c_row, bunny_col])
            else:
                is_valid_index = False

        elif d == "down":
            if 0 <= bunny_row + 1 < len(matrix):
                current_eggs = 0
                for c_row in range(bunny_row + 1, len(matrix)):
                    if matrix[c_row][bunny_col] == "X":
                        break
                    current_eggs += int(matrix[c_row][bunny_col])
                    current_pos.append([c_row, bunny_col])
            else:
                is_valid_index = False

        elif d == "left":
            if 0 <= bunny_col - 1 < len(matrix[bunny_row]):
                current_eggs = 0
                for c_col in range(bunny_col - 1, -1, -1):
                    if matrix[bunny_row][c_col] == "X":
                        break
                    current_eggs += int(matrix[bunny_row][c_col])
                    current_pos.append([bunny_row, c_col])
            else:
                is_valid_index = False

        if is_valid_index and current_eggs > max_eggs:
            max_eggs = current_eggs
            max_pos = d
            max_field_pos = current_pos.copy()

    return max_pos, max_field_pos, max_eggs


size_of_the_field = int(input())
field = [[el for el in input().split()] for _ in range(size_of_the_field)]
res = easter_bunny(field)
print(res[0])
for row in res[1]:
    print(row)
print(res[2])
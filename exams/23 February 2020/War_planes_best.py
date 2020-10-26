def are_valid_indexes(index_1, index_2, matrix):
    return index_1 in range(len(matrix)) and index_2 in range(len(matrix))


def move(plane_row, plane_col, dr, dc, matrix, steps):
    new_row, new_col = (plane_row + (dr * steps), plane_col + (dc * steps))
    if are_valid_indexes(new_row, new_col, matrix) and matrix[new_row][new_col] == ".":
        matrix[plane_row][plane_col] = "."
        matrix[new_row][new_col] = "p"
        return new_row, new_col
    else:
        return plane_row, plane_col


def shoot(plane_row, plane_col, dr, dc, matrix, targets, steps):
    new_row, new_col = plane_row + (dr * steps), plane_col + (dc * steps)
    if are_valid_indexes(new_row, new_col, matrix):
        if matrix[new_row][new_col] == "t":
            targets -= 1
        matrix[new_row][new_col] = "x"
    return targets


def war_planes(matrix, targets, plane):
    directions = {
        "right": (0, 1),
        "left": (0, -1),
        "up": (-1, 0),
        "down": (1, 0),
    }

    for _ in range(int(input())):
        plane_row, plane_col = plane
        cmd, direction, steps = input().split()
        d_row, d_col = directions[direction]
        if cmd == "move":
            plane = move(plane_row, plane_col, d_row, d_col, matrix, int(steps))
        elif cmd == "shoot":
            targets = shoot(plane_row, plane_col, d_row, d_col, matrix, targets, int(steps))
        if targets == 0:
            break

    if targets == 0:
        print(f"Mission accomplished! All {targets_count} targets destroyed.")
    else:
        print(f"Mission failed! {targets} targets left.")
    return


size = int(input())
field = []
targets_count = 0
plane_pos = ()

for i in range(size):
    field.append(input().split())
    if "p" in field[i]:
        plane_pos = (i, field[i].index("p"))
    if "t" in field[i]:
        targets_count += field[i].count("t")

war_planes(field, targets_count, plane_pos)
[print(*row) for row in field]
def is_valid(number, size):
    return 0 <= number < size


n = int(input())

bunny_pos = ()
best_sum = -999999999999999999999999
best_dir = ""
directions = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}
field = []

for row in range(n):
    line = input().split()
    if "B" in line:
        bunny_pos = (row, line.index("B"))
    field.append(line)

for direction in directions:
    current_sum = 0
    row = bunny_pos[0]
    col = bunny_pos[1]

    row_changes = directions[direction][0]
    col_changes = directions[direction][1]

    if not is_valid(row + row_changes, n) or not is_valid(col + col_changes, n):
        continue

    while is_valid(row, n) and is_valid(col, n):
        current_cell = field[row][col]
        if current_cell != "B" and current_cell != "X":
            current_sum += int(current_cell)
        elif current_cell == "X":
            break
        row += row_changes
        col += col_changes

    if current_sum > best_sum:
        best_sum = current_sum
        best_dir = direction

print(best_dir)

row_changes = directions[best_dir][0]
col_changes = directions[best_dir][1]

row = bunny_pos[0] + row_changes
col = bunny_pos[1] + col_changes

while is_valid(row, n) and is_valid(col, n):
    if field[row][col] == "X":
        break
    print([row, col])
    row += row_changes
    col += col_changes

print(best_sum)
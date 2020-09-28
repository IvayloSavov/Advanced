def is_valid(pos, rows, cols):
    return 0 <= pos[0] < rows and 0 <= pos[1] < cols


rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append([x for x in input().split()])

line = input().split()

while line[0] != "END":
    if line[0] == "swap" and len(line) == 5:
        first_pos = [int(line[1]), int(line[2])]
        second_pos = [int(line[3]), int(line[4])]

        if is_valid(first_pos, rows, cols) and is_valid(second_pos, rows, cols):
            matrix[first_pos[0]][first_pos[1]], matrix[second_pos[0]][second_pos[1]] = \
                matrix[second_pos[0]][second_pos[1]], matrix[first_pos[0]][first_pos[1]]

            for row in matrix:
                print(" ".join(row))
        else:
            print("Invalid input!")

    else:
        print("Invalid input!")
    line = input().split()
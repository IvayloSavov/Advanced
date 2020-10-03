def is_valid_index(index, __matrix):
    return 0 <= index < len(__matrix)


matrix = [[int(n) for n in input().split()] for _ in range(int(input()))]

while True:
    line = input()
    if line == "END":
        break
    line = line.split(" ")
    command, row, col, value = line[0], int(line[1]), int(line[2]), int(line[3])

    if command == "Add":
        if not is_valid_index(row, matrix) or not is_valid_index(col, matrix):
            print("Invalid coordinates")
            continue
        matrix[row][col] += value

    elif command == "Subtract":
        if not is_valid_index(row, matrix) or not is_valid_index(col, matrix):
            print("Invalid coordinates")
            continue
        matrix[row][col] -= value

[print(" ".join([str(n) for n in row])) for row in matrix]

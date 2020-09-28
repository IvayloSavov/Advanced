rows, cols = map(int, input().split(", "))

matrix = []
max_sum = -9999999999999999
max_matrix = []

for _ in range(rows):
    current_line = []
    input_line = input().split(", ")
    for e in input_line:
        current_line.append(int(e))
    matrix.append(current_line)

for i in range(rows - 1):
    for j in range(cols - 1):
        current_sum = 0
        current_matrix = []
        for k in range(i, i + 2):
            current_line = []
            for m in range(j, j + 2):
                current_sum += matrix[k][m]
                current_line.append(matrix[k][m])
            current_matrix.append(current_line)
        if current_sum > max_sum:
            max_sum = current_sum
            max_matrix = current_matrix

for row in max_matrix:
    print(" ".join(map(str, row)))

print(max_sum)
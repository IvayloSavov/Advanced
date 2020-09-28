rows, cols = map(int, input().split())

matrix = []
counter = 0

for i in range(rows):
    line = list(input().split())
    matrix.append(line)

for i in range(rows - 1):
    for j in range(cols - 1):
        if matrix[i][j + 1] == matrix[i][j] and matrix[i + 1][j + 1] == matrix[i + 1][j]:
            line_1 = matrix[i][j: j + 2]
            line_2 = matrix[i + 1][j: j + 2]
            if line_1 == line_2:
                counter += 1

print(counter)
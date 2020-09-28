from sys import maxsize

rows, cols = map(int, input().split())
matrix = []

max_sum = -maxsize
max_matrix = []

for i in range(rows):
    matrix.append([])
    line = list(map(int, input().split()))
    for c in range(cols):
        matrix[i].append(line[c])

for i in range(rows - 2):
    for j in range(cols - 2):
        current_matrix = []
        current_sum = 0
        row_index = -1
        for k in range(i, i + 3):
            current_matrix.append([])
            row_index += 1
            for m in range(j, j + 3):
                current_sum += matrix[k][m]
                current_matrix[row_index].append(matrix[k][m])
                if current_sum > max_sum:
                    max_sum = current_sum
                    max_matrix = current_matrix

print(f"Sum = {max_sum}")

for row in max_matrix:
    print(" ".join(map(str, row)))
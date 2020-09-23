n = int(input())
matrix = []

for i in range(n):
    matrix.append([int(x) for x in input().split(" ")])

diagonal_sum = 0
columns_count = len(matrix)

for i in range(columns_count):
    diagonal_sum += matrix[i][n - i - 1]

print(diagonal_sum)
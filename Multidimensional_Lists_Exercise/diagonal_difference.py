n = int(input())

primary_diagonal = 0
secondary_diagonal = 0

matrix = []

for i in range(n):
    line = list(map(int, input().split()))
    matrix.append(line)

for i in range(n):
    primary_diagonal += matrix[i][i]
    secondary_diagonal += matrix[i][n - 1 - i]

print(abs(primary_diagonal - secondary_diagonal))
rows_count, columns_count = tuple(int(x) for x in input().split(", "))
matrix = []

for _ in range(rows_count):
    matrix.append([int(x) for x in input().split(" ")])

columns_sum = [0] * columns_count

for row in range(rows_count):
    for column in range(columns_count):
        columns_sum[column] += matrix[row][column]

[print(x) for x in columns_sum]
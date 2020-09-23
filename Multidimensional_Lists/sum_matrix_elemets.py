(rows_counts, columns_count) = [int(x) for x in input().split(", ")]
matrix = []

for _ in range(rows_counts):
    row = [int(x) for x in input().split(" ")]
    matrix.append(row)

sum_rows = sum(sum(row) for row in matrix)
print(sum_rows)
print(matrix)

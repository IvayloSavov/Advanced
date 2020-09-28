rows_count, columns_count = tuple(int(x) for x in input().split(", "))
matrix = []

for _ in range(rows_count):
    matrix.append([int(x) for x in input().split(" ")])

for j in range(columns_count):  # traversing every row with j index
    total = 0
    for row in matrix:
        total += row[j]
    print(total)

# rows_count, columns_count = list(map(int, input().split(", ")))
# matrix = [list(int(n) for n in input().split()) for _ in range(rows_count)]
#
# for cow in range(columns_count):
#     sum_matrix_columns = sum(m[cow] for m in matrix)
#     print(sum_matrix_columns)

#
# def create_matrix(rows):
#     matrix = []
#     for _ in range(rows):
#         row = [int(x) for x in input().split()]
#         matrix.append(row)
#     return matrix
#
#
# def get_matrix_col_sum(matrix, rows_count, cols_count, cols_sums):
#     for row in range(rows_count):
#         for col in range(cols_count):
#             cols_sums[col] += matrix[row][col]
#     print('\n'.join([str(x) for x in col_sums]))
#
#
# rows_count, cols_count = [int(x) for x in input().split(', ')]
# matrix = create_matrix(rows_count)
# col_sums = cols_count * [0]
# get_matrix_col_sum(matrix, rows_count, cols_count, col_sums)
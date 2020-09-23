matrix = []

for _ in range(rows_count):
    matrix.append([int(x) for x in input().split(" ")])

the_sum = 0
n = len(matrix)

for row in range(n):
    for column in range(row + 1):
        the_sum += matrix[row][column]

for row in range(n):
    for column in range(n):
        if row == column:  # if row < column
            break
        the_sum += matrix[row][column]

print(the_sum)